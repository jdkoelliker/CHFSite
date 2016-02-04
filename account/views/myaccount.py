from django import forms
from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from account.models import User
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/')

    message = ''

    form = MyAccountForm(initial = {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'BirthDate': request.user.BirthDate,
        'Address1': request.user.Address1,
        'Address2': request.user.Address2,
        'City': request.user.City,
        'State': request.user.State,
        'ZipCode': request.user.ZipCode,
        'Phone': request.user.Phone,
    })
    if request.method == 'POST':
        form = MyAccountForm(request.POST)

        if form.is_valid():
            u = request.user
            u.username = form.cleaned_data.get('username')
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.email = form.cleaned_data.get('email')
            u.BirthDate = form.cleaned_data.get('BirthDate')
            u.Address1 = form.cleaned_data.get('Address1')
            u.Address2 = form.cleaned_data.get('Address2')
            u.City = form.cleaned_data.get('City')
            u.State = form.cleaned_data.get('State')
            u.ZipCode = form.cleaned_data.get('ZipCode')
            u.Phone = form.cleaned_data.get('Phone')

            u.save()

            message = 'Your changes have been saved.'

    template_vars = {
        'form': form,
        'message': message
    }

    return dmp_render_to_response(request, 'myaccount.html', template_vars)



class MyAccountForm(forms.Form):
    username = forms.CharField(label='Username', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    email = forms.CharField(label='Email', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    BirthDate = forms.CharField(label='BirthDate', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    Address1 = forms.CharField(label='Address1', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    Address2 = forms.CharField(label='Address2', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    City = forms.CharField(label='City', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    State = forms.CharField(label='State', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    ZipCode = forms.CharField(label='ZipCode', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    Phone = forms.CharField(label='Phone', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))


    def clean_Username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username = self.cleaned_data.get('username'))
            raise forms.ValidationError('This username has already been taken.')
        except User.DoesNotExist as e:
            pass
        return username
