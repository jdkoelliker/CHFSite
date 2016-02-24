# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456193625.731668
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/scripts/events.edit.jsm'
_template_uri = 'events.edit.jsm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('$( document ).ready(function() {\n\xa0\xa0\xa0\xa0$(".Delete").click(function(event) {\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0//Prevents href from executing\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0event.preventDefault();\n\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0//set variable equal to href link\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0var deleteLink = $( this ).attr( "href" );\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0//set href on new button\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0$( \'#confirm_delete_button\' ).attr( "href", deleteLink );\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0//show modal on click\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0$( \'#delete_modal\').modal( \'show\' );\n\xa0\xa0\xa0\xa0});\n});\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/scripts/events.edit.jsm", "source_encoding": "utf-8", "uri": "events.edit.jsm", "line_map": {"17": 0, "28": 22, "22": 1}}
__M_END_METADATA
"""
