# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453416188.374979
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/homepage/templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_top', 'mainbody', 'title']


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
    return runtime._inherit_from(context, 'base_app.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content_top():
            return render_content_top(context._locals(__M_locals))
        def mainbody():
            return render_mainbody(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_top'):
            context['self'].content_top(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainbody'):
            context['self'].mainbody(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_top():
            return render_content_top(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content_top">\n        <img src = "')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/Images/sunset.jpg" class = "align-center img-responsive"/>\n        <div class = "carousel-caption">\n          <div class = "wordalign" id = "mainword">\n          <h1>Contact Us</h1>\n          </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainbody(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def mainbody():
            return render_mainbody(context)
        __M_writer = context.writer()
        __M_writer('\n<div id = "contactus">\n  <div class = "container">\n    <div class = "row">\n      <div class = "col-md-offset-2 col-md-10">\n        <form action = "/homepage/contact" method = "POST">\n          <table>\n            <tr>\n              <td>Your name: <br></td>\n              <td><input type = "text" name = "yourname" size = "50" class = "form-control"/><br></td>\n            </tr>\n            <tr>\n              <td>Your email: <br></td>\n              <td><input type = "text" name = "youremail" size = "50" class = "form-control"/><br></td>\n            </tr>\n            <tr>\n              <td>Message: </td>\n              <td><textarea name = "yourmessage" cols = "50" rows = "5" class = "form-control"/></textarea><br><br></td><br>\n            </tr>\n            <tr>\n              <td></td><td><input type = "Submit" class="btn btn-success btn-md" value = "Submit" /><br><br></td>\n            </tr>\n          </table>\n        </form>\n      </div>\n    </div>\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Contact')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "contact.html", "line_map": {"68": 5, "69": 7, "70": 7, "40": 1, "76": 15, "82": 15, "45": 3, "50": 14, "55": 43, "88": 3, "100": 94, "28": 0, "61": 5, "94": 3}, "filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/homepage/templates/contact.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
