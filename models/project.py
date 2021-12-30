from odoo import models, fields, api

from odoo.exceptions import ValidationError


class ProjectInformation(models.Model):
    _inherit = 'project.project'
    members_ids = fields.One2many('member.information', 'member_id', string='Engineers Name')

    project_id = fields.Char(string="Project Id", required=True)
    project_status = fields.Selection([
        ('inprogress', 'In progress'),
        ('completed', 'Completed'),
        ('suspended', 'suspended'),
        ('other', 'Other'),
    ], default="inprogress", required=True)
    department_id = fields.Many2one('hr.department', string='Department')
    department_head_id = fields.Many2one('res.partner', string='Department Head')
    sqa_manager_id = fields.Many2one('res.partner', string='SQA Manager')
    project_owner_id = fields.Many2one('res.partner', string='Project Owner')
    project_type = fields.Selection([
        ('mid', 'Mid Size & Average'),
        ('small', 'Small size & easy'),
        ('large', 'Large size & High Complexity '),
    ], default="mid")
    created_on = fields.Datetime("Created on", readonly=True, index=True, default=fields.Datetime.now())
    project_start_date = fields.Date("Project Start Date")
    project_end_date = fields.Date("Project Close Date")
    category_id = fields.Many2one('technical.category', string='Category')
    technology_ids = fields.Many2many('technical.technology', string='Technology')

    @api.constrains('project_start_date', 'project_end_date')
    def _check_date_validation(self):
        if self.project_start_date > self.project_end_date:
            raise ValidationError('Project end date should not be previous date.')


class MemberInformation(models.Model):
    _name = 'member.information'
    _description = 'Project Information'

    employee_id = fields.Many2one('hr.employee', string='Name')
    assigned_from = fields.Date("Assigned From")
    assigned_to = fields.Date("Assigned To")
    role_id = fields.Many2one('hr.job', string="Role")
    is_manager = fields.Boolean(string="Is Manager")
    member_id = fields.Many2one('project.project')
    planned_hour = fields.Float(string='Planned Hour')
    worked_hour = fields.Float(string='Worked Hour')
    department_id = fields.Many2one('hr.department', string='Department', related='employee_id.department_id')