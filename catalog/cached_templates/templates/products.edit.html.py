# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456175543.424181
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/catalog/templates/products.edit.html'
_template_uri = 'products.edit.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['form_media', 'user_message', 'mainbody']


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
        def form_media():
            return render_form_media(context._locals(__M_locals))
        def user_message():
            return render_user_message(context._locals(__M_locals))
        message = context.get('message', UNDEFINED)
        def mainbody():
            return render_mainbody(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'form_media'):
            context['self'].form_media(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainbody'):
            context['self'].mainbody(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'user_message'):
            context['self'].user_message(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_media(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def form_media():
            return render_form_media(context)
        __M_writer = context.writer()
        __M_writer(' ')
        __M_writer(str( form_media ))
        __M_writer(' ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_user_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def user_message():
            return render_user_message(context)
        message = context.get('message', UNDEFINED)
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
        __M_writer('\n  <div class = "container">\n    <div class = "row">\n      <div class = "col-md-9">\n        <h2>Update product information below</h2>\n      </div>\n      <div class = "col-md-3">\n        <br><br><a href="/catalog/products/">Back to the Product List &raquo</a>\n      </div>\n    </div><hr><br><br>\n    <div class = "row">\n      <div class = "col-md-offset-1 col-md-11">\n        <form method="POST">\n          <table>\n            ')
        __M_writer(str( form))
        __M_writer('\n          </table>\n          <br>\n          <input type= "submit" class="col-md-offset-1 btn btn-success btn-lg" value="Save Changes"/><br><br>\n        </form>\n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/catalog/templates/products.edit.html", "line_map": {"51": 27, "68": 3, "69": 3, "70": 3, "41": 1, "76": 29, "46": 3, "108": 102, "102": 19, "83": 29, "84": 30, "85": 31, "86": 35, "56": 37, "100": 5, "28": 0, "93": 5, "62": 3, "101": 19}, "uri": "products.edit.html"}
__M_END_METADATA
"""
