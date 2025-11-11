# -*- coding: utf-8 -*-
# from odoo import http


# class Unitatva(http.Controller):
#     @http.route('/unitatva/unitatva', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unitatva/unitatva/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('unitatva.listing', {
#             'root': '/unitatva/unitatva',
#             'objects': http.request.env['unitatva.unitatva'].search([]),
#         })

#     @http.route('/unitatva/unitatva/objects/<model("unitatva.unitatva"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unitatva.object', {
#             'object': obj
#         })

