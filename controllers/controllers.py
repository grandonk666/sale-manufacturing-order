# -*- coding: utf-8 -*-
# from odoo import http


# class SalesOrderManufacturingButton(http.Controller):
#     @http.route('/sales_order_manufacturing_button/sales_order_manufacturing_button/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_order_manufacturing_button/sales_order_manufacturing_button/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_order_manufacturing_button.listing', {
#             'root': '/sales_order_manufacturing_button/sales_order_manufacturing_button',
#             'objects': http.request.env['sales_order_manufacturing_button.sales_order_manufacturing_button'].search([]),
#         })

#     @http.route('/sales_order_manufacturing_button/sales_order_manufacturing_button/objects/<model("sales_order_manufacturing_button.sales_order_manufacturing_button"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_order_manufacturing_button.object', {
#             'object': obj
#         })
