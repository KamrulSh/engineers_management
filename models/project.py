from odoo import models, fields, api


class ProjectInformation(models.Model):
    _inherit = 'project.project'
    members_ids = fields.One2many('member.information', 'member_id', string='Engineers Name')


class MemberInformation(models.Model):
    _name = 'member.information'
    _description = 'Project Information'

    name = fields.Many2one('hr.employee', string='Name')
    assigned_from = fields.Date("Assigned From")
    assigned_to = fields.Date("Assigned To")
    role = fields.Many2one('hr.job', string="Role")
    is_manager = fields.Boolean(string="Is Manager")
    member_id = fields.Many2one('project.project')
