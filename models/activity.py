from odoo import models , fields, api
from datetime import datetime
from odoo.exceptions import ValidationError


class Activity(models.Model):
    _name = 'ikplaner_activity'
    _description = 'Activity'

    name = fields.Char('Nombre Activiadad', requiered = True)
    creator = fields.Char(string='Creador' , default=lambda self: self.env.user.name)
    activity_start = fields.Date(string = 'Fecha de inicio', default = datetime.today() , requiered = True)
    activity_end = fields.Date(string = 'Fecha de fin' , requiered = True)
    priority = fields.Selection([
        ('ninguna' , 'Ninguna'),
        ('baja' , 'Baja'),
        ('media' , 'Media'),
        ('alta' , 'Alta')],
        'Prioridad' , default ="ninguna")
    members = fields.Many2many('res.partner' , string='Miembros')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            raise ValidationError('Debe especificar un nombre para la actividad.')
        if not vals.get('activity_start'):
            raise ValidationError('Debe especificar una fecha de inicio para la actividad.')
        if not vals.get('activity_end'):
            raise ValidationError('Debe especificar una fecha de finalización para la actividad.')
        if vals.get('activity_end') <= vals.get('activity_start'):
            raise ValidationError('La fecha de finalización debe ser posterior a la fecha de inicio.')
        if not vals.get('members'):
            vals.update({'members': [(4, self.env.user.partner_id.id)]})
        return super(Activity, self).create(vals)


    @api.model
    def write(self, vals):
        if vals.get('activity_end') and vals.get('activity_end') <= self.activity_start:
            raise ValidationError('La fecha de finalización debe ser posterior a la fecha de inicio.')
        if vals.get('name') is None:
            raise ValidationError('Debe especificar un nombre para la actividad.')
        if vals.get('activity_start') is None:
            raise ValidationError('Debe especificar una fecha de inicio para la actividad.')
        if vals.get('activity_end') is None:
            raise ValidationError('Debe especificar una fecha de finalización para la actividad.')
        if not vals.get('members'):
            vals.update({'members': [(4, self.env.user.partner_id.id)]})
        return super(Activity, self).write(vals)
