# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456243323.860535
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/templates/users.html'
_template_uri = 'users.html'
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
        users = context.get('users', UNDEFINED)
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
        __M_writer('Users')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainbody(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def mainbody():
            return render_mainbody(context)
        __M_writer = context.writer()
        __M_writer('\n<div class = "container">\n  <div class = "row">\n    <div class = "col-md-10">\n      <h2>Users List</h2>\n    </div>\n    <div class = "col-md-2">\n      <p class = "text-right">\n        <a href = "/manager/users.create/" class = "btn btn-success">Create User</a>\n      </p>\n    </div>\n  </div><hr>\n</div>\n<div id = "userslist">\n  <div class = "container">\n    <div class = "row">\n      <div class = "col-md-12">\n        <table class= "table table-striped">\n          <tr>\n            <th>Username</th>\n            <th>First Name</th>\n            <th>Last Name</th>\n            <th>Email</th>\n            <th>Phone</th>\n            <th>Group</th>\n            <th>BirthDate</th>\n            <th></th>\n            <th>Password</th>\n            <th>Manage</th>\n          </tr>\n')
        for user in users:
            __M_writer('            <tr>\n              <td>')
            __M_writer(str( user.username))
            __M_writer('</td>\n              <td>')
            __M_writer(str( user.first_name))
            __M_writer('</td>\n              <td>')
            __M_writer(str( user.last_name))
            __M_writer('</td>\n              <td>')
            __M_writer(str( user.email))
            __M_writer('</td>\n              <td>')
            __M_writer(str( user.Phone))
            __M_writer('</td>\n              <td>\n')
            for group in user.groups.all():
                __M_writer('                ')
                __M_writer(str( group.name))
                __M_writer('<br>\n')
            __M_writer('              </td>\n              <td>')
            __M_writer(str( user.BirthDate))
            __M_writer('</td>\n              <td></td>\n              <td>\n              <a href = "/manager/users.changepassword/')
            __M_writer(str( user.id ))
            __M_writer('/">Change</a></td>\n              <td>\n                <a href = "/manager/users.edit/')
            __M_writer(str( user.id ))
            __M_writer('/">Edit</a>\n                |\n                <a href = "/manager/users.delete/')
            __M_writer(str(user.id))
            __M_writer('/" class = "Delete">Delete</a>\n              </td>\n            </tr>\n')
        __M_writer('        </table>\n      </div>\n    </div>\n  </div><br><br>\n</div>\n\n\n<div class="modal fade" id = "delete_modal" tabindex="-1" role="dialog">\n  <div class="modal-dialog" role = "document">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type = "button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n        <h4 class="modal-title">Delete</h4>\n      </div>\n      <div class="modal-body">\n        <p>Are you sure you want to delete this user?</p>\n      </div>\n      <div class="modal-footer">\n        <a class="btn btn-default" data-dismiss="modal">Cancel</a>\n        <a id = "confirm_delete_button" class="btn btn-success">Delete User</a>\n      </div>\n    </div><!-- /.modal-content -->\n  </div><!-- /.modal-dialog -->\n</div><!-- /.modal -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/templates/users.html", "uri": "users.html", "line_map": {"66": 5, "73": 5, "74": 35, "75": 36, "76": 37, "77": 37, "78": 38, "79": 38, "80": 39, "81": 39, "82": 40, "83": 40, "84": 41, "85": 41, "86": 43, "87": 44, "88": 44, "89": 44, "90": 46, "91": 47, "28": 0, "93": 50, "94": 50, "95": 52, "96": 52, "97": 54, "98": 54, "99": 58, "38": 1, "92": 47, "43": 3, "48": 82, "54": 3, "105": 99, "60": 3}}
__M_END_METADATA
"""
