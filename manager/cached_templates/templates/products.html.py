# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456243807.895289
_enable_loop = True
_template_filename = '/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['mainbody', 'title']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def mainbody():
            return render_mainbody(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
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


def render_mainbody(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def mainbody():
            return render_mainbody(context)
        __M_writer = context.writer()
        __M_writer('\n<div class = "container">\n  <div class = "row">\n    <div class = "col-md-10">\n      <h2>Product List</h2>\n    </div>\n    <div class = "col-md-2">\n      <p class = "text-right">\n        <a href = "/manager/products.create/" class = "btn btn-success">Create Product</a>\n      </p>\n    </div>\n  </div><hr>\n</div>\n<div id = "productlist">\n  <div class = "container">\n    <div class = "row">\n      <div class = "col-md-12">\n        <table class= "table table-striped">\n          <tr>\n            <th>Name</th>\n            <th>Type</th>\n            <th>Image</th>\n            <th>Quantity</th>\n            <th></th>\n            <th>Manage</th>\n          </tr>\n')
        for product in products:
            __M_writer('            <tr>\n              <td>')
            __M_writer(str( product.name))
            __M_writer('</td>\n              <td>')
            __M_writer(str( product.__class__.__name__))
            __M_writer('</td>\n              <td style = "max-width:30px"><img src = "')
            __M_writer(str(STATIC_URL))
            __M_writer('/manager/media/product_images/')
            __M_writer(str( product.image ))
            __M_writer('" class = "img-responsive"></td>\n              <td>\n')
            if product.__class__.__name__ == 'BulkProduct':
                __M_writer('                  <span class = "quantity">')
                __M_writer(str( product.quantity))
                __M_writer('</span>\n                  <a href = "/manager/products.get_quantity/')
                __M_writer(str( product.id ))
                __M_writer('" data-id= "')
                __M_writer(str(product.id))
                __M_writer('" class = "glyphicon glyphicon-refresh refresh_button"></a>\n')
            __M_writer('              </td>\n              <td></td>\n              <td>\n                <a href = "/manager/products.edit/')
            __M_writer(str( product.id ))
            __M_writer('/">Edit</a>\n                |\n                <a href = "/manager/products.delete/')
            __M_writer(str( product.id ))
            __M_writer('/" class = "Delete">Delete</a>\n              </td>\n            </tr>\n')
        __M_writer('        </table>\n      </div>\n    </div>\n  </div><br><br>\n</div>\n\n\n<div class="modal fade" id = "delete_modal" tabindex="-1" role="dialog">\n  <div class="modal-dialog" role = "document">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type = "button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n        <h4 class="modal-title">Delete</h4>\n      </div>\n      <div class="modal-body">\n        <p>Are you sure you want to delete this user?</p>\n      </div>\n      <div class="modal-footer">\n        <a class="btn btn-default" data-dismiss="modal">Cancel</a>\n        <a id = "confirm_delete_button" class="btn btn-success">Delete User</a>\n      </div>\n    </div><!-- /.modal-content -->\n  </div><!-- /.modal-dialog -->\n</div><!-- /.modal -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Products')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/Users/JohnKoelliker/Desktop/PythonProjects/CHFSite/manager/templates/products.html", "line_map": {"64": 31, "65": 32, "66": 33, "67": 33, "68": 34, "69": 34, "70": 35, "71": 35, "72": 35, "73": 35, "74": 37, "75": 38, "76": 38, "77": 38, "78": 39, "79": 39, "80": 39, "81": 39, "82": 41, "83": 44, "84": 44, "85": 46, "86": 46, "87": 50, "28": 0, "93": 3, "99": 3, "39": 1, "105": 99, "44": 3, "49": 74, "55": 5, "63": 5}, "uri": "products.html"}
__M_END_METADATA
"""
