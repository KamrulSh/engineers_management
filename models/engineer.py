from odoo import models, fields, api


class EngineerInformation(models.Model):
    _inherit = 'hr.employee'
    _description = 'Engineers Information'

    engineer_id = fields.Integer(string="Engineer ID", tracking=True)
    engineer_type = fields.Selection([
        ('parttime', 'Part time'),
        ('fulltime', 'Full time'),
        ('contract', 'Contract')
    ], default="fulltime", tracking=True)

    skype_id = fields.Char(string="Skype ID")
    joining_date = fields.Date("Joining Date", tracking=True)
    blood_group = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ], default="A+")
