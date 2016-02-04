# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454609543.334072
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/account/templates/changepassword.html'
_template_uri = 'changepassword.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_top', 'user_message', 'mainbody']


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
        form = context.get('form', UNDEFINED)
        def user_message():
            return render_user_message(context._locals(__M_locals))
        def mainbody():
            return render_mainbody(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        message = context.get('message', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_top'):
            context['self'].content_top(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainbody'):
            context['self'].mainbody(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'user_message'):
            context['self'].user_message(**pageargs)
        

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
        __M_writer('\n<div class="content_top">\n    <img src = "')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/Images/forest.jpg" class = "align-center img-responsive"/>\n    <div class = "carousel-caption">\n      <div class = "wordalign" id = "mainword">\n        <h1>My Account</h1>\n      </div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_user_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        message = context.get('message', UNDEFINED)
        def user_message():
            return render_user_message(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if message != '':
            __M_writer('  <div class="alert alert-success alert-dismissible" role="alert">\n    <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n    <strong>Success!</strong> Your changes have been saved.\n  </div>\n')
        else:
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainbody(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def mainbody():
            return render_mainbody(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <div class = "container">\n    <div class = "row">\n    <h2>Update password information below</h2><hr>\n      <div class = "col-md-offset-1 col-md-11">\n        <form action="/account/changepassword" method="POST">\n          <table id = "myform">\n            ')
        __M_writer(str( form.as_table() ))
        __M_writer('\n          </table>\n          <br>\n          <input type= "submit" class="col-md-offset-1 btn btn-success btn-lg" href="account/changepassword/" value="Save Changes"/>\n          <a class="btn btn-info btn-sm" href="account/myaccount/" role="button">Return back to My Account &raquo</a>\n        </form><br>\n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "changepassword.html", "filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/account/templates/changepassword.html", "line_map": {"102": 13, "70": 3, "71": 5, "72": 5, "42": 1, "103": 20, "110": 104, "78": 31, "47": 12, "104": 20, "52": 29, "85": 31, "86": 32, "87": 33, "88": 37, "57": 39, "95": 13, "28": 0, "63": 3}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
