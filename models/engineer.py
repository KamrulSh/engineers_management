from odoo import models, fields, api


class EngineerInformation(models.Model):
    _inherit = 'hr.employee'
    _description = 'Engineers Information'

    skype_id = fields.Char(string="Skype ID")
    joining_date = fields.Date("Joining Date")
