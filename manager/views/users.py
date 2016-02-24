from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
from django.contrib.auth import authenticate, login
from .. import dmp_render, dmp_render_to_response
from account import models as amod
from django import forms
import datetime
from django.conf import settings
from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, Group


@view_function
def process_request(request):

    users = amod.User.objects.all().order_by('last_name', 'first_name')

    template_vars = {
        'users': users
    }

    return dmp_render_to_response(request, 'users.html', template_vars)

#########################################################################################
######## Editing a User #########
@permission_required('account.change_user', login_url = '/homepage/index/')
@view_function
def edit(request):

    try:
        user = amod.User.objects.get(id=request.urlparams[0])
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/manager/users/')

    message = ''

    form = EditForm(initial = model_to_dict(user))
    if request.method == 'POST':
        form = EditForm(request.POST)
        form.request = request
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.BirthDate = form.cleaned_data.get('BirthDate')
            user.Address1 = form.cleaned_data.get('Address1')
            user.Address2 = form.cleaned_data.get('Address2')
            user.City = form.cleaned_data.get('City')
            user.State = form.cleaned_data.get('State')
            user.ZipCode = form.cleaned_data.get('ZipCode')
            user.Phone = form.cleaned_data.get('Phone')


            user.save()

            user.groups.clear()
            user.user_permissions.clear()
            for group in form.cleaned_data['groups']:
                user.groups.add(group)
            for permission in form.cleaned_data['permissions']:
                user.user_permissions.add(permission)


            message = 'Your changes have been saved.'

    template_vars = {
        'form': form,
        'message': message
    }

    return dmp_render_to_response(request, 'users.edit.html', template_vars)

class EditForm(forms.Form):
    username = forms.CharField(label='Username', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    email = forms.CharField(label='Email', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    BirthDate = forms.DateField(label='BirthDate', required = True, widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    Address1 = forms.CharField(label='Address1', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    Address2 = forms.CharField(label='Address2', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    City = forms.CharField(label='City', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    State = forms.CharField(label='State', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    ZipCode = forms.CharField(label='ZipCode', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    Phone = forms.CharField(label='Phone', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    groups = forms.ModelMultipleChoiceField(label = 'Groups', required = False, queryset = Group.objects.all(), widget = forms.CheckboxSelectMultiple)
    permissions = forms.ModelMultipleChoiceField(label = 'Permissions', required = False, queryset = Permission.objects.all(), widget = forms.CheckboxSelectMultiple)

    def clean(self):
        return self.cleaned_data

    def clean_Username(self):
        uid = self.request.urlparams[0]
        username = self.cleaned_data.get('username')

        if amod.User.objects.filter(username= username).exclude(id = uid).count() >0:
            raise forms.ValidationError('Already taken...')
        return username

#########################################################################################
####### Creating a User ###########
@permission_required('account.add_user', login_url = '/homepage/index/')
@view_function
def create(request):


  form = CreateForm()
  if request.method == 'POST':
      form = CreateForm(request.POST)
      if form.is_valid():
          #create the user here
          u = amod.User()
          u.username = form.cleaned_data.get('username')
          u.first_name = form.cleaned_data.get('first_name')
          u.last_name = form.cleaned_data.get('last_name')
          u.BirthDate = form.cleaned_data.get('BirthDate')
          u.Phone = form.cleaned_data.get('Phone')
          u.set_password(form.cleaned_data.get('password'))

          u.save()

          return HttpResponse('''
            <script>
                window.location.href = '/manager/users/';
            </script>
          ''')



  template_vars = {
    'form': form,
  }

  return dmp_render_to_response(request, 'users.create.html', template_vars)



class CreateForm(forms.Form):
    username = forms.CharField(label='Username', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    BirthDate = forms.DateField(label='BirthDate', required = True, widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    Phone = forms.CharField(label='Phone', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    password = forms.CharField(label='Password', required = True, max_length=100, widget = forms.PasswordInput(attrs= { 'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', required = True, max_length=100, widget = forms.PasswordInput(attrs= { 'class': 'form-control'}))

    def clean_Username(self):
        username = self.cleaned_data.get('username')
        try:
            user = amod.User.objects.get(username = self.cleaned_data.get('username'))
            raise forms.ValidationError('This username has already been taken.')
        except amod.User.DoesNotExist as e:
            pass
        return username

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your passwords need to match. Please try again.')
        return self.cleaned_data


############# Delete a User ##############
@permission_required('account.delete_user', login_url = '/homepage/index/')
@view_function
def delete(request):
    #Deletes a user
    try:
        user = amod.User.objects.get(id = request.urlparams[0])
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/manager/users/')

    #delete the user
    user.delete()

    return HttpResponseRedirect('/manager/users/')


#########################################################################################
####### Changing a Password ###########

@view_function
def changepassword(request):

    message = ''

    try:
        user = amod.User.objects.get(id=request.urlparams[0])
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/manager/users/')


    form = ChangePasswordForm()
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        form.request = request
        if form.is_valid():

             #user = request.User()

             newpassword = form.cleaned_data.get('newpassword')

             user.set_password(form.cleaned_data.get('newpassword'))

             user.save()

             user = authenticate(username = user.username, password = newpassword)
             if user is not None:
                 #login(request, user)
                 message = 'Your changes have been saved.'

    template_vars = {
        'form': form,
        'message': message,
    }

    return dmp_render_to_response(request, 'users.changepassword.html', template_vars)



class ChangePasswordForm(forms.Form):

    newpassword = forms.CharField(label='New Password', required = True, max_length=100, widget = forms.PasswordInput(attrs= { 'class': 'form-control'}))
    newpassword2 = forms.CharField(label='Confirm New Password', required = True, max_length=100, widget = forms.PasswordInput(attrs= { 'class': 'form-control'}))

    def clean(self):
        if self.cleaned_data.get('newpassword') != self.cleaned_data.get('newpassword2'):
            raise forms.ValidationError('Your passwords need to match. Please try again.')
        return self.cleaned_data
