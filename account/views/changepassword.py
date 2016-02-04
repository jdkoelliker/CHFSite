from django import forms
from django.conf import settings
from django_mako_plus.controller import view_function
from django.contrib.auth import authenticate, login
from .. import dmp_render, dmp_render_to_response
from account.models import User
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
  message = ''

  form = ChangePasswordForm(initial = {
  })
  if request.method == 'POST':
      form = ChangePasswordForm(request.POST)
      form.request = request
      if form.is_valid():
           user = request.user

           newpassword = form.cleaned_data.get('newpassword')

           user.set_password(form.cleaned_data.get('newpassword'))

           message = 'Your changes have been saved.'

           user.save()

           user = authenticate(username = user.username, password = newpassword)
           if user is not None:
               login(request, user)

  template_vars = {
    'form': form,
    'message': message
  }

  return dmp_render_to_response(request, 'changepassword.html', template_vars)



class ChangePasswordForm(forms.Form):

    currentpassword = forms.CharField(label='Current Password', required = True, max_length=100, widget = forms.PasswordInput(attrs= { 'class': 'form-control'}))
    newpassword = forms.CharField(label='New Password', required = True, max_length=100, widget = forms.PasswordInput(attrs= { 'class': 'form-control'}))
    newpassword2 = forms.CharField(label='Confirm New Password', required = True, max_length=100, widget = forms.PasswordInput(attrs= { 'class': 'form-control'}))

    def clean_currentpassword(self):
        u = self.request.user
        if not u.check_password(self.cleaned_data.get('currentpassword')):
            raise forms.ValidationError('Try your current password again.')
        return self.cleaned_data.get('currentpassword')

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your passwords need to match. Please try again.')
        return self.cleaned_data
