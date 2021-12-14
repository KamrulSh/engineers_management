from odoo import models, fields, api, _


class Employee(models.Model):
    _inherit = 'project.project'

    @api.model
    def get_dept_employee(self):
        cr = self._cr
        cr.execute("""select department_id, hr_department.name,count(*) 
            from project_project join hr_department on hr_department.id=project_project.department_id 
            group by project_project.department_id,hr_department.name""")
        fetch_data = cr.fetchall()
        data = []
        for i in range(0, len(fetch_data)):
            data.append({'label': fetch_data[i][1], 'value': fetch_data[i][2]})

        return data
