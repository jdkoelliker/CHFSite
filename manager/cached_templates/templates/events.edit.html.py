# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456195072.425587
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/templates/events.edit.html'
_template_uri = 'events.edit.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['mainbody', 'user_message', 'form_media']


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
        def user_message():
            return render_user_message(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        def mainbody():
            return render_mainbody(context._locals(__M_locals))
        message = context.get('message', UNDEFINED)
        def form_media():
            return render_form_media(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
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


def render_mainbody(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        areas = context.get('areas', UNDEFINED)
        def mainbody():
            return render_mainbody(context)
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <div class = "container">\n    <div class = "row">\n      <div class = "col-md-9">\n        <h2>Update event information below</h2>\n      </div>\n      <div class = "col-md-3">\n        <br><br><a href="/manager/events/">Back to the Event List &raquo</a>\n      </div>\n    </div><hr><br>\n    <div class = "row">\n      <div class = "col-md-offset-1 col-md-11">\n        <form method="POST">\n          <table>\n            ')
        __M_writer(str( form))
        __M_writer('\n          </table>\n          <br>\n          <input type= "submit" class="col-md-offset-1 btn btn-success btn-lg" value="Save Changes"/><br><br><br>\n        </form>\n      </div>\n    </div>\n    <div class = "row">\n      <div class = "col-md-9">\n        <h2>Areas Associated with Event</h2>\n      </div>\n      <div class = "col-md-3">\n        <br><br><a class = "btn btn-md btn-success" href="/manager/events.create_area/')
        __M_writer(str(request.urlparams[0] ))
        __M_writer('">Create a New Area for this Event &raquo</a>\n      </div>\n    </div><hr><br>\n    <div class = "row">\n      <div class = "col-md-12">\n        <table class= "table table-striped">\n          <tr>\n            <th>Name</th>\n            <th>Description</th>\n            <th></th>\n            <th>Manage</th>\n          </tr>\n')
        for area in areas:
            __M_writer('            <tr>\n              <td>')
            __M_writer(str( area.name))
            __M_writer('</td>\n              <td>')
            __M_writer(str( area.description))
            __M_writer('</td>\n              <td></td>\n              <td>\n                <a href = "/manager/events.delete_area/')
            __M_writer(str( area.id ))
            __M_writer('/')
            __M_writer(str(request.urlparams[0] ))
            __M_writer('" class = "Delete"> Delete</a>\n              </td>\n            </tr>\n')
        __M_writer('        </table>\n      </div>\n    </div>\n  </div>\n\n<div class="modal fade" id = "delete_modal" tabindex="-1" role="dialog">\n  <div class="modal-dialog" role = "document">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type = "button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n        <h4 class="modal-title">Delete</h4>\n      </div>\n      <div class="modal-body">\n        <p>Are you sure you want to delete this area?</p>\n      </div>\n      <div class="modal-footer">\n        <a class="btn btn-default" data-dismiss="modal">Cancel</a>\n        <a id = "confirm_delete_button" class="btn btn-success">Delete Area</a>\n      </div>\n    </div><!-- /.modal-content -->\n  </div><!-- /.modal-dialog -->\n</div><!-- /.modal -->\n')
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


def render_form_media(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def form_media():
            return render_form_media(context)
        __M_writer = context.writer()
        __M_writer(' ')
        __M_writer(str(form.media))
        __M_writer(' ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "events.edit.html", "filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/templates/events.edit.html", "line_map": {"64": 5, "73": 5, "74": 19, "75": 19, "76": 31, "77": 31, "78": 43, "79": 44, "80": 45, "81": 45, "82": 46, "83": 46, "84": 49, "85": 49, "86": 49, "87": 49, "88": 53, "28": 0, "94": 77, "101": 77, "102": 78, "103": 79, "104": 83, "43": 1, "111": 3, "48": 3, "53": 75, "118": 3, "119": 3, "120": 3, "58": 85, "126": 120}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
