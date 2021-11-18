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
    technicalSkill_ids = fields.One2many('technical.skill', 'skill_id', string="Technical skill")


class EngineerPosition(models.Model):
    _name = 'engineer.position'
    _description = 'Engineer Position'
    _rec_name = 'position_name'

    position_name = fields.Char(string="Role")


class TechnicalSkill(models.Model):
    _name = 'technical.skill'
    _description = 'Technical Skill'

    year_experience = fields.Integer(string="Experience")
    skill_level = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),

    ], default="A")
    category_id = fields.Many2one('technical.category', string="Category")
    technology_id = fields.Many2one('technical.technology', string="Technology")
    skill_id = fields.Many2one('hr.employee', string='skills')


class Category(models.Model):
    _name = 'technical.category'
    _description = 'Technical Category'
    _rec_name = 'category_name'

    category_name = fields.Char(string="Category name")


class Technology(models.Model):
    _name = 'technical.technology'
    _description = 'Technology'
    _rec_name = 'technology_name'

    technology_name = fields.Char(string="Technology name")
