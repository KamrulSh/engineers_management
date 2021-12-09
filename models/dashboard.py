from odoo import models, fields, api, _


class Employee(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def get_dept_employee(self):
        data = [{'label': "Java developer", 'value': 3}, {'label': "Odoo developer", 'value': 5},
                {'label': "JS developer", 'value': 2},
                {'label': "iOS developer", 'value': 4}]
        return data
