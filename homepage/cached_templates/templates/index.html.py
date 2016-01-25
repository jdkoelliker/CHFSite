# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453416189.344775
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_right', 'content_left', 'content_top', 'content_main', 'title']


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
        def title():
            return render_title(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_main():
            return render_content_main(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_top'):
            context['self'].content_top(**pageargs)
        

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
        __M_writer('\n  <h2>Watch</h2><hr/>\n  <h4>Learn more about our Colonial Heritage by watching this video.</h4></br>\n  <div class="embed-responsive embed-responsive-4by3">\n    <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/N_S-vsXrtQE" frameborder="0" allowfullscreen></iframe>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\n  <h2>Volunteer</h2><hr/>\n  <h4>We have had tremendous support from our volunteers over the years. Check out these facts about our events in past years!</h4></br>\n  <div class="progress">\n    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width: 70%">\n        2013 - 132 Total Volunteers\n      <span class="sr-only">70% Complete</span>\n    </div>\n  </div>\n  <div class="progress">\n    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 83%">\n        2014 - 169 Total Volunteers\n      <span class="sr-only">83% Complete (warning)</span>\n    </div>\n  </div>\n  <div class="progress">\n    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: 100%">\n      2015 - 243 Total Volunteers\n      <span class="sr-only">100% Complete (danger)</span>\n    </div>\n  </div>\n  <p style = "text-align: center"><a class="btn btn-info btn-md" href="#" role="button">Volunteer Today &raquo</a>\n')
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
        __M_writer('homepage/media/Images/farm.jpg" class = "align-center img-responsive"/>\n        <div class = "carousel-caption">\n          <div class = "wordalign" id = "mainwords">\n            <h1>Colonial Heritage Foundation</h1>\n            <h3>Redefining the way we celebrate history.</h3><br/>\n            <p><a class="btn btn-success btn-lg" href="#" role="button">Learn More &raquo</a>\n          </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_main():
            return render_content_main(context)
        __M_writer = context.writer()
        __M_writer('\n  <h2>News</h2><hr/>\n  <h4>Festival Quickly Approaching</h4>\n  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>\n  <h4>New CHF Online Store Coming Soon</h4>\n  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>\n  <h4>Restructuring the CHF Board</h4>\n  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "line_map": {"64": 47, "99": 4, "132": 3, "69": 54, "81": 48, "108": 6, "106": 4, "75": 48, "44": 1, "138": 132, "49": 3, "114": 39, "107": 6, "54": 15, "87": 16, "120": 39, "59": 38, "28": 0, "93": 16, "126": 3}, "filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/homepage/templates/index.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
