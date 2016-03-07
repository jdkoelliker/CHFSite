from django import forms
from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from account.models import User
from django.http import HttpResponseRedirect, HttpResponse

@view_function
def process_request(request):


  form = CreateAccountForm()
  if request.method == 'POST':
      form = CreateAccountForm(request.POST)
      if form.is_valid():
          #create the user here
          u = User()
          u.username = form.cleaned_data.get('username')
          u.first_name = form.cleaned_data.get('first_name')
          u.last_name = form.cleaned_data.get('last_name')
          u.BirthDate = form.cleaned_data.get('BirthDate')
          u.Phone = form.cleaned_data.get('Phone')
          u.set_password(form.cleaned_data.get('password'))

          u.save()

          return HttpResponse('''
            <script>
                window.location.href = '/homepage/index/';
            </script>
          ''')



  template_vars = {
    'form': form,
  }

  return dmp_render_to_response(request, 'createaccount.html', template_vars)



class CreateAccountForm(forms.Form):
    username = forms.CharField(label='Username', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    BirthDate = forms.CharField(label='BirthDate', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    Phone = forms.CharField(label='Phone', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    password = forms.CharField(label='Password', required = True, max_length=100, widget = forms.PasswordInput(attrs= { 'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', required = True, max_length=100, widget = forms.PasswordInput(attrs= { 'class': 'form-control'}))

    def clean_Username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username = self.cleaned_data.get('username'))
            raise forms.ValidationError('This username has already been taken.')
        except User.DoesNotExist as e:
            pass
        return username

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your passwords need to match. Please try again.')
        return self.cleaned_data


    # method #3
    # if Users.objects.filter(username = username).count()>0:
    #     raise forms.ValidationError('This username has already been taken.')
    # return username


    # def clean_Username(self):
    #     Username = self.cleaned_data.get('Username')
    #     if not Username.lower().startswith('a'):
    #         er = forms.ValidationError('Please start your username with the letter "a".')
    #         raise er
    #     return username
