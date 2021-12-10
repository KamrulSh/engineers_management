from odoo import models, fields, api, _


class Employee(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def get_dept_employee(self):
        cr = self._cr
        cr.execute("""select department_id, hr_department.name,count(*) 
            from hr_employee join hr_department on hr_department.id=hr_employee.department_id 
            group by hr_employee.department_id,hr_department.name""")
        fetch_data = cr.fetchall()
        data = []
        for i in range(0, len(fetch_data)):
            data.append({'label': fetch_data[i][1], 'value': fetch_data[i][2]})

        return data
