# -*- coding: utf-8 -*-
# from odoo import http


# class ActivityPlanner(http.Controller):
#     @http.route('/activity_planner/activity_planner', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/activity_planner/activity_planner/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('activity_planner.listing', {
#             'root': '/activity_planner/activity_planner',
#             'objects': http.request.env['activity_planner.activity_planner'].search([]),
#         })

#     @http.route('/activity_planner/activity_planner/objects/<model("activity_planner.activity_planner"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('activity_planner.object', {
#             'object': obj
#         })
