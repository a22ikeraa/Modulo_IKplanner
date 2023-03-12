from odoo import models , fields, api
from datetime import datetime


class Activity(models.Model):
    _name = 'IKPlaner.activity'
    _description = 'Activity'

    name = fields.Char('Nombre Activiadad', requiered = True)
    creator = fields.Char(string='Creador' , default=lambda self: self.env.user.name)
    activity_start = fields.Date(string = 'Fecha de inicio', default = datetime.today())
    activity_end = fields.Date(string = 'Fecha de fin')
    priority = fields.Selection([
        ('ninguna' , 'Ninguna'),
        ('baja' , 'Baja'),
        ('media' , 'Media'),
        ('alta' , 'Alta')],
        'Prioridad' , default ="ninguna")
    members = fields.Many2many('res.partner' , string='Miembros')

    
    