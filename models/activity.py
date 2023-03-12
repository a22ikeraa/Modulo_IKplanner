from odoo import models , fields, api
from datetime import datetime


class Activity(models.Model):
    _name = 'ikplaner_activity'
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



    @api.model
    def action_save(self):
    # save changes
        self.ensure_one()
    # perform any necessary validation
        self.write({
           'name': self.name,
           'description': self.description,
        })
       # perform any other necessary operations
        return True  

    @api.model
    def action_cancel(self):
    # discard changes
       self.ensure_one()
       # perform any necessary operations
       return True
    