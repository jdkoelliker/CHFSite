from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from account.models import User
from django.http import HttpResponse, HttpResponseRedirect

@view_function
def process_request(request):

  if request.user.is_authenticated():
      return HttpResponseRedirect('/homepage/index/')


  form = LoginForm()
  if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():

          login(request, form.user)

          return HttpResponse('''
            <script>
                window.location.href = '/homepage/index/';
            </script>
          ''')

  template_vars = {
    'form': form,
  }

  return dmp_render_to_response(request, 'login.html', template_vars)



class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    password = forms.CharField(label='Password', required = True, max_length=100, widget = forms.PasswordInput(attrs= { 'class': 'form-control'}))


    def clean(self):
        user = authenticate(username = self.cleaned_data.get('username'), password = self.cleaned_data.get('password'))
        if user == None:
            raise forms.ValidationError('This username and password does not match our records. Please try again.')
        self.user = user
        return self.cleaned_data
