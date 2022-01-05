from odoo import models, fields, api, _


class ProjectDashboard(models.TransientModel):
    _name = 'project.invoice.wizard'

    project_id = fields.Many2one('project.project', string="Project name", required=True)


