from odoo import models, fields, api
from lxml import etree
from odoo.exceptions import ValidationError


class EngineerInformation(models.Model):
    _inherit = 'hr.employee'
    _description = 'Engineers Information'

    engineer_id = fields.Char(string="Engineer ID")
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
    technicalSkill_ids = fields.One2many('technical.skill', 'skill_id', string="Technical skill")
    project_id = fields.Many2one('project.project')

    @api.constrains('engineer_id')
    def _check_engineer_id_validation(self):
        if self.engineer_id.isnumeric():
            digit = len(self.engineer_id)
            zero = 5 - digit
            if digit < 5:
                id_after_zero = "0" * zero + self.engineer_id
                self.engineer_id = id_after_zero
            elif digit > 5:
                raise ValidationError('Digit can not be greater than 5.')
        else:
            raise ValidationError('Not number.')

    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        result = super().fields_view_get(view_id=view_id, view_type=view_type,
                                       toolbar=toolbar, submenu=submenu)
        if view_type == 'form':
            doc = etree.XML(result['arch'])
            id_reference = doc.xpath("//field[@name='engineer_id']")
            if id_reference:
                id_reference[0].set("string", "Engineer Unique id")
                id_reference[0].addnext(etree.Element('label', {'string': '5 Digit Id'}))
                result['arch'] = etree.tostring(doc, encoding='unicode')

        return result


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
