# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454608806.725716
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['footer', 'content_right', 'mainbody', 'main_menu', 'maintenance_message', 'title', 'content_left', 'content_top', 'user_message', 'entirebody', 'mainjumbo', 'content_main']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def footer():
            return render_footer(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def mainbody():
            return render_mainbody(context._locals(__M_locals))
        def main_menu():
            return render_main_menu(context._locals(__M_locals))
        def maintenance_message():
            return render_maintenance_message(context._locals(__M_locals))
        def user_message():
            return render_user_message(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def content_main():
            return render_content_main(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content_top():
            return render_content_top(context._locals(__M_locals))
        def entirebody():
            return render_entirebody(context._locals(__M_locals))
        def mainjumbo():
            return render_mainjumbo(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n\n    <link rel="icon" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/Images/flagicon.ico" type="image/x-icon"/>\n    <title> CHF - ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\n\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n\n    <!--THIS IS HOW YOU LINK TO A BOOTSTRAP STYLESHEET!!!!-->\n    <link rel= "stylesheet" href = "')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/Bootstrap/css/bootstrap.min.css"/>\n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\n  </head>\n  <body>\n    <div id = "maintenance_message">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintenance_message'):
            context['self'].maintenance_message(**pageargs)
        

        __M_writer('\n\n    </div>\n  <header>\n    <div id = "main_menu">\n      <nav class="navbar navbar-inverse">\n        <div class="container-fluid">\n          <!-- Brand and toggle get grouped for better mobile display -->\n          <div class="navbar-header">\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n              <span class="sr-only">Toggle navigation</span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n            </button>\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_menu'):
            context['self'].main_menu(**pageargs)
        

        __M_writer('\n          </div><!-- /.navbar-collapse -->\n      </div><!-- /.container-fluid -->\n    </nav>\n    </div>\n    <div id = "user_message">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'user_message'):
            context['self'].user_message(**pageargs)
        

        __M_writer('\n    </div>\n  </header>\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'entirebody'):
            context['self'].entirebody(**pageargs)
        

        __M_writer('\n  <!-- Latest compiled and minified JavaScript -->\n  <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('homepage/media/bootstrap/js/bootstrap.min.js"></script>\n  <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n  <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\n\n')
        __M_writer('  ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('      ')

        import datetime
        current_year =  datetime.date.today().year
              
        
        __M_writer('\n      Copyright &copy; John Koelliker ')
        __M_writer(str(current_year))
        __M_writer('\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainbody(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        def mainbody():
            return render_mainbody(context)
        def content_main():
            return render_content_main(context)
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\n      <div class = "container">\n        <div class="row">\n          <div class = "col-md-3">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n          </div>\n          <div class = "col-md-6">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_main'):
            context['self'].content_main(**pageargs)
        

        __M_writer('\n          </div>\n          <div class = "col-md-3">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n          </div>\n        </div>\n      </div>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_menu():
            return render_main_menu(context)
        __M_writer = context.writer()
        __M_writer('\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintenance_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintenance_message():
            return render_maintenance_message(context)
        __M_writer = context.writer()
        __M_writer('\n            SITE UNDER MAINTENANCE\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_top():
            return render_content_top(context)
        __M_writer = context.writer()
        __M_writer('\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_user_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def user_message():
            return render_user_message(context)
        __M_writer = context.writer()
        __M_writer('\n        <div class="alert alert-danger alert-dismissible" role="alert">\n          <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n          <strong>Alert!</strong> This is a dismissable user alert message.\n        </div>\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entirebody(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        def content_right():
            return render_content_right(context)
        def mainbody():
            return render_mainbody(context)
        def content_left():
            return render_content_left(context)
        def content_top():
            return render_content_top(context)
        def entirebody():
            return render_entirebody(context)
        def mainjumbo():
            return render_mainjumbo(context)
        def content_main():
            return render_content_main(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainjumbo'):
            context['self'].mainjumbo(**pageargs)
        

        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainbody'):
            context['self'].mainbody(**pageargs)
        

        __M_writer('\n  <footer>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n  </footer>\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainjumbo(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_top():
            return render_content_top(context)
        def mainjumbo():
            return render_mainjumbo(context)
        __M_writer = context.writer()
        __M_writer('\n        <div class = "jumbotron">\n          <div class="container">\n            <div class = "row">\n              <div class = "col-md-12">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_top'):
            context['self'].content_top(**pageargs)
        

        __M_writer('\n              </div>\n            </div>\n          </div>\n      </div>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_main():
            return render_content_main(context)
        __M_writer = context.writer()
        __M_writer('\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/homepage/templates/base.htm", "line_map": {"132": 84, "262": 59, "138": 72, "267": 71, "272": 89, "17": 4, "19": 0, "277": 98, "150": 72, "155": 77, "218": 65, "160": 81, "283": 60, "165": 85, "308": 80, "296": 66, "171": 44, "302": 80, "177": 44, "51": 2, "52": 4, "53": 5, "183": 27, "57": 5, "58": 12, "59": 12, "189": 27, "64": 13, "65": 16, "66": 19, "67": 19, "68": 22, "69": 22, "70": 22, "314": 308, "75": 29, "224": 65, "206": 76, "80": 45, "291": 60, "212": 76, "85": 56, "90": 100, "91": 102, "92": 102, "93": 103, "94": 103, "95": 104, "96": 104, "97": 107, "98": 107, "99": 107, "230": 51, "195": 13, "105": 91, "236": 51, "111": 91, "112": 93, "113": 93, "242": 59, "118": 96, "119": 97, "120": 97, "126": 84}, "source_encoding": "utf-8", "uri": "base.htm"}
__M_END_METADATA
"""
