# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453416020.23243
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/homepage/templates/base_app.htm'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def main_menu():
            return render_main_menu(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_menu'):
            context['self'].main_menu(**pageargs)
        

        __M_writer('\n\n\n')
        __M_writer('\n')
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_menu():
            return render_main_menu(context)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <!-- Collect the nav links, forms, and other content for toggling -->\n      </div>\n        <a href="/homepage/index"><img src= "')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/Images/CHFLogo.png" id = "mainimage" class="navbar-brand img-responsive"></a>\n        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n          <ul class="nav navbar-nav">\n            <li class= "')
        __M_writer(str( 'active' if request.dmp_router_page == 'index' else ''))
        __M_writer('"><a href="/homepage/index">Home <span class="sr-only">(current)</span></a></li>\n            <li class= "')
        __M_writer(str( 'active' if request.dmp_router_page == 'about' else ''))
        __M_writer('"><a href="/homepage/about">About</a></li>\n            <li class= "')
        __M_writer(str( 'active' if request.dmp_router_page == 'contact' else ''))
        __M_writer('"><a href="/homepage/contact">Contact</a></li>\n            <li class= "')
        __M_writer(str( 'active' if request.dmp_router_page == 'terms' else ''))
        __M_writer('"><a href="/homepage/terms">Terms</a></li>\n            <li class= "')
        __M_writer(str( 'active' if request.dmp_router_page == 'faq' else ''))
        __M_writer('"><a href="/homepage/faq">FAQ</a></li>\n            <li class= "')
        __M_writer(str( 'active' if request.dmp_router_page == 'sections' else ''))
        __M_writer('"><a href="/homepage/sections">Sections</a></li>\n          </ul>\n          <ul class="nav navbar-nav navbar-right">\n            <li class="dropdown">\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Welcome John!<span class="caret"></span></a>\n              <ul class="dropdown-menu">\n                <li><a href="#">Events</a></li>\n                <li><a href="#">Learn More</a></li>\n                <li><a href="#">FAQ</a></li>\n                <li role="separator" class="divider"></li>\n                <li><a href="#">My Account</a></li>\n                <li role="separator" class="divider"></li>\n                <li><a href="#">Log Out</a></li>\n              </ul>\n            </li>\n          </ul>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base_app.htm", "line_map": {"64": 10, "65": 11, "66": 11, "67": 12, "68": 12, "69": 13, "70": 13, "71": 14, "72": 14, "78": 72, "28": 0, "37": 1, "42": 31, "43": 35, "44": 39, "50": 3, "58": 3, "59": 6, "60": 6, "61": 9, "62": 9, "63": 10}, "filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/homepage/templates/base_app.htm", "source_encoding": "utf-8"}
__M_END_METADATA
"""
