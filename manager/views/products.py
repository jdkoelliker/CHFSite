from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
from django.contrib.auth import authenticate, login
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from account import models as amod
from django import forms
import datetime
from django.conf import settings
from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, Group


@view_function
def process_request(request):

    products = cmod.Product.objects.all().order_by('name')

    template_vars = {
        'products': products
    }

    return dmp_render_to_response(request, 'products.html', template_vars)


#########################################################################################
######## Editing a Product #########
@permission_required('catalog.change_product', login_url = '/homepage/index/')
@view_function
def edit(request):

    try:
        product = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/manager/products/')

    message = ''


    initial = model_to_dict(product)
    initial['ptype'] = product.__class__.__name__
    form = EditForm(initial =initial)

    if request.method == 'POST':
        form = EditForm(request.POST)
        form.request = request
        if form.is_valid():

            if form.cleaned_data.get('ptype') == 'RentalProduct':
                product.status = form.cleaned_data.get('status')
            elif form.cleaned_data.get('ptype') == 'BulkProduct':
                product.quantity = form.cleaned_data.get('quantity')
            elif form.cleaned_data.get('ptype') == 'IndividualProduct':
                product.creator = form.cleaned_data.get('creator')

            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.price = form.cleaned_data.get('price')
            product.add_date = form.cleaned_data.get('add_date')
            product.image = form.cleaned_data.get('image')

            product.save()

            message = 'Your changes have been saved.'

    template_vars = {
        'form': form,
        'message': message,
        'pid': product.id,
    }

    return dmp_render_to_response(request, 'products.edit.html', template_vars)

RENTAL_STATUS_CHOICES = (
    ('current', 'Rentable'),
    ('damaged', 'Damaged'),
    ('retired','No Longer Rentable')
)

PRODUCT_TYPE_CHOICES = (
    ('RentalProduct', 'Rental Product'),
    ('IndividualProduct', 'Individual Product'),
    ('BulkProduct', 'Bulk Product'),
)

class EditForm(forms.Form):
    name = forms.CharField(label='Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    description = forms.CharField(label='Description', required = True, max_length=100, widget = forms.Textarea(attrs= { 'class': 'form-control'}))
    price = forms.CharField(label='Price', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    image = forms.CharField(label='Image', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    status = forms.ChoiceField(label='Status', required = False, choices = RENTAL_STATUS_CHOICES, widget = forms.Select(attrs= { 'class': 'form-control'}))
    quantity = forms.IntegerField(label='Quantity', required = False, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    creator = forms.ModelChoiceField(label='Creator', required = False, queryset = amod.User.objects.order_by('last_name', 'first_name'), widget = forms.Select(attrs= { 'class': 'form-control'}))
    ptype = forms.ChoiceField(label = "Product Type", required = True, choices = PRODUCT_TYPE_CHOICES, widget = forms.HiddenInput(attrs= { 'class': 'form-control'}))

    def clean(self):
        return self.cleaned_data


#########################################################################################
####### Creating a Product ###########
@permission_required('catalog.add_product', login_url = '/homepage/index/')
@view_function
def create(request):




    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            #create the product here
            product = cmod.Product()

            if form.cleaned_data.get('ptype') == 'RentalProduct':
              product.status = form.cleaned_data.get('status')
            elif form.cleaned_data.get('ptype') == 'BulkProduct':
              product.quantity = form.cleaned_data.get('quantity')
            elif form.cleaned_data.get('ptype') == 'IndividualProduct':
              product.creator = form.cleaned_data.get('creator')

            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.price = form.cleaned_data.get('price')
            product.add_date = form.cleaned_data.get('add_date')
            product.image = form.cleaned_data.get('image')
            product.save()

            return HttpResponse('''
            <script>
                window.location.href = '/manager/products/';
            </script>
            ''')



    template_vars = {
        'form': form,
    }

    return dmp_render_to_response(request, 'products.create.html', template_vars)

RENTAL_STATUS_CHOICES = (
    ('current', 'Rentable'),
    ('damaged', 'Damaged'),
    ('retired','No Longer Rentable')
)
PRODUCT_TYPE_CHOICES = (
    ('RentalProduct', 'Rental Product'),
    ('IndividualProduct', 'Individual Product'),
    ('BulkProduct', 'Bulk Product'),
)

class CreateForm(forms.Form):
    name = forms.CharField(label='Name', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    description = forms.CharField(label='Description', required = True, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    price = forms.CharField(label='Price', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    image = forms.CharField(label='Image', required = False, max_length=100, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    ptype = forms.ChoiceField(label = 'Product Type', required = True, choices = PRODUCT_TYPE_CHOICES, widget = forms.Select(attrs= { 'class': 'form-control'}))
    status = forms.ChoiceField(label='Status', required = False, choices = RENTAL_STATUS_CHOICES, widget = forms.Select(attrs= { 'class': 'form-control'}))
    quantity = forms.IntegerField(label='Quantity', required = False, widget = forms.TextInput(attrs= { 'class': 'form-control'}))
    creator = forms.ModelChoiceField(label='Creator', required = False, queryset = amod.User.objects.order_by('last_name', 'first_name'), widget = forms.Select(attrs= { 'class': 'form-control'}))



############# Delete a User ##############
@permission_required('catalog.delete_product', login_url = '/homepage/index/')
@view_function
def delete(request):
    #Deletes a product
    try:
        product = cmod.Product.objects.get(id = request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/manager/products/')

    #delete the product
    product.delete()

    return HttpResponseRedirect('/manager/products/')



################################
@view_function
def get_quantity(request):
    try:
        product = cmod.Product.objects.get(id = request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return Http404()
    return HttpResponse(product.quantity)
