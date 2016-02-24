# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456253048.596389
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/templates/venues.edit.html'
_template_uri = 'venues.edit.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['form_media', 'mainbody', 'user_message']


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
        def mainbody():
            return render_mainbody(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def user_message():
            return render_user_message(context._locals(__M_locals))
        message = context.get('message', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(' ')
        __M_writer(str(form.media))
        __M_writer(' ')
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
        __M_writer('\n  <div class = "container">\n    <div class = "row">\n      <div class = "col-md-9">\n        <h2>Update venue information below</h2>\n      </div>\n      <div class = "col-md-3">\n        <br><br><a href="/manager/venues/">Back to the Venue List &raquo</a>\n      </div>\n    </div><hr><br><br>\n    <div class = "row">\n      <div class = "col-md-offset-1 col-md-11">\n        <form method="POST">\n          <table>\n            ')
        __M_writer(str( form))
        __M_writer('\n          </table>\n          <br>\n          <input type= "submit" class="col-md-offset-1 btn btn-success btn-lg" value="Save Changes"/><br><br>\n        </form>\n      </div>\n    </div>\n  </div>\n')
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


"""
__M_BEGIN_METADATA
{"filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/templates/venues.edit.html", "line_map": {"99": 29, "100": 30, "69": 3, "70": 3, "71": 3, "41": 1, "77": 5, "46": 3, "109": 102, "92": 29, "51": 27, "84": 5, "85": 19, "86": 19, "56": 37, "28": 0, "102": 35, "62": 3, "101": 31}, "source_encoding": "utf-8", "uri": "venues.edit.html"}
__M_END_METADATA
"""
