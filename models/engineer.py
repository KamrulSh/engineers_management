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
    position_id = fields.Many2one('engineer.position', string="Role")


class EngineerPosition(models.Model):
    _name = 'engineer.position'
    _description = 'Engineer Position'
    _rec_name = 'position_name'

    position_name = fields.Char(string="Role")
