from odoo import models, fields, api


class ProjectInformation(models.Model):
    _inherit = 'project.project'
    _description = 'Project Information'

    members_ids = fields.Many2many('hr.employee', 'project_id', string='Engineers Name')
