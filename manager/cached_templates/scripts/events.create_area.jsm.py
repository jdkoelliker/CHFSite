# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456191979.026598
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/scripts/events.create_area.jsm'
_template_uri = 'events.create_area.jsm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer("$(function() {\n\n  $('#createareaform').ajaxForm({\n\n      target: '#jquery-loadmodal-js-body',\n\n  });//click\n\n});\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/scripts/events.create_area.jsm", "source_encoding": "utf-8", "uri": "events.create_area.jsm", "line_map": {"17": 0, "28": 22, "22": 1}}
__M_END_METADATA
"""
