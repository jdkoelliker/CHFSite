from django import forms
from django.conf import settings
from django.contrib.auth import logout
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from account.models import User
from django.http import HttpResponseRedirect

@view_function
def process_request(request):

    logout(request)

    return HttpResponseRedirect('/homepage/index/')
