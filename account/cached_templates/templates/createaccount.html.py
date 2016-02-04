# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454622936.783164
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/account/templates/createaccount.html'
_template_uri = 'createaccount.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <form action="/account/createaccount/" id = "createaccountform" method="POST">\n    <table id = "myform">\n      ')
        __M_writer(str( form.as_table() ))
        __M_writer('\n    </table>\n    <div class = "container">\n      <div class = "row">\n        <div class = "col-md-offset-1">\n          <br><input type="submit" class="btn btn-info btn-sm" value="Create Account"/>\n        </div>\n      </div>\n    </div>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"36": 1, "54": 3, "55": 6, "56": 6, "41": 16, "28": 0, "62": 56, "47": 3}, "filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/account/templates/createaccount.html", "source_encoding": "utf-8", "uri": "createaccount.html"}
__M_END_METADATA
"""
