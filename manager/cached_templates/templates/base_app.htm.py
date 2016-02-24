# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456243854.75271
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/templates/base_app.htm'
_template_uri = 'base_app.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['main_menu']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def main_menu():
            return render_main_menu(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_menu'):
            context['self'].main_menu(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def main_menu():
            return render_main_menu(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <!-- Collect the nav links, forms, and other content for toggling -->\n      </div>\n        <a href="/homepage/index"><img src= "')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/Images/CHFLogo.png" id = "mainimage" class="navbar-brand img-responsive"></a>\n        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n          <ul class="nav navbar-nav">\n            <li class= "')
        __M_writer(str( 'active' if request.dmp_router_page == 'index' else ''))
        __M_writer('"><a href="/homepage/index/">Home <span class="sr-only">(current)</span></a></li>\n            <li class= "')
        __M_writer(str( 'active' if request.dmp_router_page == 'users' else ''))
        __M_writer('"><a href="/manager/users/">Users</a></li>\n            <li class= "')
        __M_writer(str( 'active' if request.dmp_router_page == 'products' else ''))
        __M_writer('"><a href="/manager/products/">Products</a></li>\n            <li class= "')
        __M_writer(str( 'active' if request.dmp_router_page == 'venues' else ''))
        __M_writer('"><a href="/manager/venues/">Venues</a></li>\n            <li class= "')
        __M_writer(str( 'active' if request.dmp_router_page == 'events' else ''))
        __M_writer('"><a href="/manager/events/">Events</a></li>\n          </ul>\n\n          <ul class="nav navbar-nav navbar-right">\n')
        if request.user.is_authenticated():
            __M_writer('              <li class="dropdown">\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"> Welcome, ')
            __M_writer(str( request.user))
            __M_writer('!<span class="caret"></span></a>\n                <ul class="dropdown-menu">\n                  <li><a href="/manager/users/">Manage Site</a></li>\n                  <li><a href="#">Learn More</a></li>\n                  <li><a href="#">FAQ</a></li>\n                  <li role="separator" class="divider"></li>\n                  <li><a href="/account/myaccount/">My Account</a></li>\n                  <li role="separator" class="divider"></li>\n                  <li><a href="/account/logout/">Log Out</a></li>\n                </ul>\n              </li>\n')
        else:
            __M_writer('              <li id = "loginbutton"><a>Login</a></li>\n              <li id = "createaccountbutton"><a>Create Account</a></li>\n')
        __M_writer('\n          </ul>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base_app.htm", "line_map": {"64": 11, "65": 12, "66": 12, "67": 13, "68": 13, "69": 17, "70": 18, "71": 19, "72": 19, "73": 30, "74": 31, "75": 34, "81": 75, "28": 0, "37": 1, "42": 37, "48": 3, "56": 3, "57": 6, "58": 6, "59": 9, "60": 9, "61": 10, "62": 10, "63": 11}, "filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/templates/base_app.htm", "source_encoding": "utf-8"}
__M_END_METADATA
"""
