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

    events = emod.Event.objects.all().order_by('name')

    template_vars = {
        'events': events
    }

    return dmp_render_to_response(request, 'events.html', template_vars)

#########################################################################################
######## Editing an Event #########
@permission_required('event.change_event', login_url = '/homepage/index/')
@view_function
def edit(request):

    try:
        event = emod.Event.objects.get(id=request.urlparams[0])
        areas = emod.Area.objects.filter(event_id = event.id).order_by('name')
    except emod.Event.DoesNotExist:
        return HttpResponseRedirect('/manager/events/')

    message = ''



    form = EditForm(initial = {
        'name': event.name,
        'description': event.description,
        'start_date': event.start_date,
        'end_date': event.end_date,
        'venue': event.venue,
    })
    if request.method == 'POST':
        form = EditForm(request.POST)
        form.request = request
        if form.is_valid():
            event.name = form.cleaned_data.get('name')
            event.description = form.cleaned_data.get('description')
            event.start_date = form.cleaned_data.get('start_date')
            event.end_date = form.cleaned_data.get('end_date')
            event.venue = form.cleaned_data.get('venue')

            event.save()

            message = 'Your changes have been saved.'

    template_vars = {
        'form': form,
        'message': message,
        'areas': areas,
    }

    return dmp_render_to_response(request, 'events.edit.html', template_vars)

class EditForm(forms.Form):
    name = forms.CharField(label='Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    description = forms.CharField(label='Description', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    start_date = forms.DateField(label='BirthDate', required = True, widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    end_date = forms.DateField(label='BirthDate', required = True, widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    venue = forms.ModelChoiceField(label='Venue', required = False, queryset = emod.Venue.objects.order_by('name'), widget = forms.Select(attrs= { 'class': 'form-control'}))
    #venue = forms.CharField(label='Venue', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))

    def clean(self):
        return self.cleaned_data


#########################################################################################
####### Creating an Event ###########
@permission_required('event.add_event', login_url = '/homepage/index/')
@view_function
def create(request):


  form = CreateForm()
  if request.method == 'POST':
      form = CreateForm(request.POST)
      if form.is_valid():
          #create the user here
          event = emod.Event()
          event.name = form.cleaned_data.get('name')
          event.description = form.cleaned_data.get('description')
          event.start_date = form.cleaned_data.get('start_date')
          event.end_date = form.cleaned_data.get('end_date')
          event.venue = form.cleaned_data.get('venue')


          event.save()

          return HttpResponse('''
            <script>
                window.location.href = '/manager/events/';
            </script>
          ''')



  template_vars = {
    'form': form,
  }

  return dmp_render_to_response(request, 'events.create.html', template_vars)



class CreateForm(forms.Form):
    name = forms.CharField(label='Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    description = forms.CharField(label='Description', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    start_date = forms.DateField(label='Start Date', required = True, widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    end_date = forms.DateField(label='End Date', required = True, widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    venue = forms.ModelChoiceField(label='Venue', required = False, queryset = emod.Venue.objects.order_by('name'), widget = forms.Select(attrs= { 'class': 'form-control'}))
    #venue = forms.CharField(label='Venue', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))


############# Delete a Event ##############
@permission_required('event.delete_event', login_url = '/homepage/index/')
@view_function
def delete(request):
    #Deletes a user
    try:
        event = emod.Event.objects.get(id = request.urlparams[0])
    except emod.Event.DoesNotExist:
        return HttpResponseRedirect('/manager/events/')

    #delete the user
    event.delete()

    return HttpResponseRedirect('/manager/events/')

############# Delete an Area ##############
@permission_required('event.delete_area', login_url = '/homepage/index/')
@view_function
def delete_area(request):
    #Deletes a user
    try:
        area = emod.Area.objects.get(id = request.urlparams[0])
    except emod.Event.DoesNotExist:
        return HttpResponseRedirect('/manager/events/')

    #delete the user
    area.delete()

    eventid = request.urlparams[1]
    url = "/manager/events.edit/" + eventid

    return HttpResponseRedirect(url)



################# CREATE AN AREA ######################
@permission_required('event.add_area', login_url = '/homepage/index/')
@view_function
def create_area(request):


  form = CreateAreaForm()
  if request.method == 'POST':
      form = CreateAreaForm(request.POST)
      if form.is_valid():
          #create the user here
          area = emod.Area()
          area.name = form.cleaned_data.get('name')
          area.description = form.cleaned_data.get('description')
          area.place_number = form.cleaned_data.get('place_number')
          area.event = emod.Event.objects.get(id = request.urlparams[0])


          area.save()

          eventid = request.urlparams[0]
          url = "/manager/events.edit/" + eventid

          return HttpResponseRedirect(url)



  template_vars = {
    'form': form,
  }

  return dmp_render_to_response(request, 'events.create_area.html', template_vars)



class CreateAreaForm(forms.Form):
    name = forms.CharField(label='Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    description = forms.CharField(label='Description', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    place_number = forms.CharField(label='Place Number', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
