# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456182730.461068
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/event/templates/venues.html'
_template_uri = 'venues.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'mainbody']


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
        def title():
            return render_title(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        def mainbody():
            return render_mainbody(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainbody'):
            context['self'].mainbody(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Venues')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainbody(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        def mainbody():
            return render_mainbody(context)
        __M_writer = context.writer()
        __M_writer('\n<div class = "container">\n  <div class = "row">\n    <div class = "col-md-10">\n      <h2>Venue List</h2>\n    </div>\n    <div class = "col-md-2">\n      <p class = "text-right">\n        <a href = "/event/venues.create/" class = "btn btn-success">Create Venue</a>\n      </p>\n    </div>\n  </div><hr>\n</div>\n<div id = "productlist">\n  <div class = "container">\n    <div class = "row">\n      <div class = "col-md-12">\n        <table class= "table table-striped">\n          <tr>\n            <th>Name</th>\n            <th>Address</th>\n            <th></th>\n            <th>Manage</th>\n          </tr>\n')
        for product in products:
            __M_writer('            <tr>\n              <td>')
            __M_writer(str( product.name))
            __M_writer('</td>\n              <td>')
            __M_writer(str( product.address))
            __M_writer('</td>\n              <td></td>\n              <td>\n                <a href = "/event/venues.edit/')
            __M_writer(str( product.id ))
            __M_writer('/">Edit</a>\n                |\n                <a href = "/event/venues.delete/')
            __M_writer(str( product.id ))
            __M_writer('/" class = "Delete">Delete</a>\n              </td>\n            </tr>\n')
        __M_writer('        </table>\n      </div>\n    </div>\n  </div><br><br>\n</div>\n\n\n<div class="modal fade" id = "delete_modal" tabindex="-1" role="dialog">\n  <div class="modal-dialog" role = "document">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type = "button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n        <h4 class="modal-title">Delete</h4>\n      </div>\n      <div class="modal-body">\n        <p>Are you sure you want to delete this user?</p>\n      </div>\n      <div class="modal-footer">\n        <a class="btn btn-default" data-dismiss="modal">Cancel</a>\n        <a id = "confirm_delete_button" class="btn btn-success">Delete User</a>\n      </div>\n    </div><!-- /.modal-content -->\n  </div><!-- /.modal-dialog -->\n</div><!-- /.modal -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/event/templates/venues.html", "source_encoding": "utf-8", "line_map": {"80": 35, "66": 5, "43": 3, "38": 1, "73": 5, "74": 29, "75": 30, "76": 31, "77": 31, "28": 0, "79": 32, "48": 65, "81": 35, "82": 37, "83": 37, "84": 41, "78": 32, "54": 3, "90": 84, "60": 3}, "uri": "venues.html"}
__M_END_METADATA
"""
