# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453416620.475835
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/homepage/templates/sections.html'
_template_uri = 'sections.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_right', 'content_left', 'mainjumbo', 'content_main', 'title']


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
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def mainjumbo():
            return render_mainjumbo(context._locals(__M_locals))
        def content_main():
            return render_content_main(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainjumbo'):
            context['self'].mainjumbo(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_main'):
            context['self'].content_main(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\n  <div id = "content_right">\n    Right Content\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\n  <div id = "content_left">\n    Left Content\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainjumbo(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def mainjumbo():
            return render_mainjumbo(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class = "container">\n    <div id = "mainjumbo">\n      Top Content\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_main():
            return render_content_main(context)
        __M_writer = context.writer()
        __M_writer('\n<div id = "content_main">\n    Main Content\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Sections')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "sections.html", "line_map": {"128": 3, "80": 22, "98": 5, "68": 26, "134": 128, "104": 5, "28": 0, "74": 22, "43": 1, "110": 17, "48": 3, "116": 17, "53": 11, "86": 12, "58": 16, "92": 12, "122": 3, "63": 21}, "filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/homepage/templates/sections.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
