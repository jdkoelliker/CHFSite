from django.conf import settings
from django_mako_plus.controller import view_function

from .. import dmp_render, dmp_render_to_response

@view_function
def process_request(request):

  print('>>>Your name was: ', request.POST.get('yourname'))
  print('>>>Your email was: ', request.POST.get('youremail'))
  print('>>>Your message was: ', request.POST.get('yourmessage'))

  template_vars = {

    'clientname': request.POST.get('yourname'),
    'clientemail': request.POST.get('youremail'),
    'clientmessage': request.POST.get('yourmessage'),

  }
  return dmp_render_to_response(request, 'contact.html', template_vars)
