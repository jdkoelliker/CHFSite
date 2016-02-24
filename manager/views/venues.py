from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
from django.contrib.auth import authenticate, login
from .. import dmp_render, dmp_render_to_response
from account import models as amod
from event import models as emod
from django import forms
import datetime
from django.conf import settings
from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, Group



@view_function
def process_request(request):

    venues = emod.Venue.objects.all().order_by('name')

    template_vars = {
        'venues': venues,
    }

    return dmp_render_to_response(request, 'venues.html', template_vars)

#########################################################################################
######## Editing a Venue #########
@permission_required('event.change_venue', login_url = '/homepage/index/')
@view_function
def edit(request):

    try:
        venue = emod.Venue.objects.get(id=request.urlparams[0])
    except emod.Venue.DoesNotExist:
        return HttpResponseRedirect('/manager/venues/')

    message = ''

    form = EditForm(initial = {
        'name': venue.name,
        'address': venue.address,
        'city': venue.city,
        'state': venue.state,
        'zip_code': venue.zip_code
    })
    if request.method == 'POST':
        form = EditForm(request.POST)
        form.request = request
        if form.is_valid():
            venue.name = form.cleaned_data.get('name')
            venue.description = form.cleaned_data.get('address')
            venue.start_date = form.cleaned_data.get('city')
            venue.end_date = form.cleaned_data.get('state')
            venue.event = form.cleaned_data.get('zip_code')

            venue.save()

            message = 'Your changes have been saved.'

    template_vars = {
        'form': form,
        'message': message
    }

    return dmp_render_to_response(request, 'venues.edit.html', template_vars)

class EditForm(forms.Form):
    name = forms.CharField(label='Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    address = forms.CharField(label='Address', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    city = forms.CharField(label='City', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    state = forms.CharField(label='State', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    zip_code = forms.CharField(label='Zip Code', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))


    def clean(self):
        return self.cleaned_data


#########################################################################################
####### Creating a Venue ###########
@permission_required('event.add_venue', login_url = '/homepage/index/')
@view_function
def create(request):


  form = CreateForm()
  if request.method == 'POST':
      form = CreateForm(request.POST)
      if form.is_valid():
          #create the user here
          venue = emod.Venue()
          venue.name = form.cleaned_data.get('name')
          venue.address = form.cleaned_data.get('address')
          venue.city = form.cleaned_data.get('city')
          venue.state = form.cleaned_data.get('state')
          venue.zip_code = form.cleaned_data.get('zip_code')

          venue.save()

          return HttpResponse('''
            <script>
                window.location.href = '/manager/venues/';
            </script>
          ''')



  template_vars = {
    'form': form,
  }

  return dmp_render_to_response(request, 'venues.create.html', template_vars)



class CreateForm(forms.Form):
    name = forms.CharField(label='Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    address = forms.CharField(label='Address', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    city = forms.CharField(label='City', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    state = forms.CharField(label='State', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    zip_code = forms.CharField(label='Zip Code', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))


############# Delete a User ##############
@permission_required('event.delete_venue', login_url = '/homepage/index/')
@view_function
def delete(request):
    #Deletes a user
    try:
        venue = emod.Venue.objects.get(id = request.urlparams[0])
    except emod.Venue.DoesNotExist:
        return HttpResponseRedirect('/manager/venues/')

    #delete the user
    venue.delete()

    return HttpResponseRedirect('/manager/venues/')
