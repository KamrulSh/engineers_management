from odoo import models, fields, api


class ProjectInformation(models.Model):
    _inherit = 'project.project'
    members_ids = fields.One2many('member.information', 'member_id', string='Engineers Name')

    project_status = fields.Selection([
        ('inprogress', 'In progress'),
        ('completed', 'Completed'),
        ('suspended', 'suspended'),
        ('other', 'Other'),
    ], default="inprogress")
    department = fields.Many2one('hr.department', string='Department')
    department_head = fields.Many2one('res.partner', string='Department Head')
    sqa_manager = fields.Many2one('res.partner', string='SQA Manager')
    project_owner = fields.Many2one('res.partner', string='Project Owner')
    project_type = fields.Selection([
        ('mid', 'Mid Size & Average'),
        ('small', 'Small size & easy'),
        ('large', 'Large size & High Complexity '),
    ], default="mid")
    estimated_effort = fields.Float(string='Estimated Effort')
    actual_effort = fields.Float(string='Actual Effort')
    created_on = fields.Datetime("Created on", readonly=True, index=True, default=fields.Datetime.now())
    project_start_date = fields.Date("Project Start Date")
    project_end_date = fields.Date("Project Close Date")
    category_id = fields.Many2one('technical.category', string='Category')
    technology_ids = fields.Many2many('technical.technology', string='Technology')


class MemberInformation(models.Model):
    _name = 'member.information'
    _description = 'Project Information'

    name = fields.Many2one('hr.employee', string='Name')
    assigned_from = fields.Date("Assigned From")
    assigned_to = fields.Date("Assigned To")
    role = fields.Many2one('hr.job', string="Role")
    is_manager = fields.Boolean(string="Is Manager")
    member_id = fields.Many2one('project.project')
