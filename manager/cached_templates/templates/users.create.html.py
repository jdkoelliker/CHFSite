# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456156723.114934
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/templates/users.create.html'
_template_uri = 'users.create.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['mainbody', 'form_media']


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
        def mainbody():
            return render_mainbody(context._locals(__M_locals))
        def form_media():
            return render_form_media(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'form_media'):
            context['self'].form_media(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainbody'):
            context['self'].mainbody(**pageargs)
        

        __M_writer('\n')
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
        __M_writer('\n  <div class = "container">\n    <div class = "row">\n    <h2>Create New User</h2><hr>\n      <div class = "col-md-offset-1 col-md-11">\n        <form method="POST">\n          <table>\n            ')
        __M_writer(str( form ))
        __M_writer('\n          </table>\n          <br>\n          <input type= "submit" class="col-md-offset-1 btn btn-success btn-lg" value="Create User"/>\n        </form><br>\n      </div>\n      <div class = "col-md-offset-2 col-md-10">\n        <a href="/manager/users">Back to the Users List &raquo</a><br><br>\n      </div>\n    </div>\n  </div>\n')
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
        __M_writer(str( form.media ))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/templates/users.create.html", "uri": "users.create.html", "source_encoding": "utf-8", "line_map": {"48": 23, "82": 76, "38": 1, "54": 5, "69": 3, "76": 3, "43": 3, "28": 0, "61": 5, "62": 12, "63": 12}}
__M_END_METADATA
"""
