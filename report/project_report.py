from odoo import models, fields, api


class ProjectTaskDetails(models.Model):
    _name = "project.info.details"
    _auto = False
    _rec_name = 'employee'

    # It is for project task details

    # project = fields.Many2one('project.project')
    # task = fields.Char(string='Task')
    # manager = fields.Many2one('res.users')
    # partner = fields.Many2one('res.partner', string='Customer')
    # date_deadline = fields.Char(string='Task Deadline')

    # def init(self):
    #     self._cr.execute("""
    #         CREATE OR REPLACE VIEW project_task_details AS (
    #             SELECT row_number() OVER () as id,
    #             ps.project_id as project,
    #             ps.name as task,
    #             ps.date_deadline as date_deadline,
    #             pp.partner_id as partner,
    # 			  pp.user_id as manager
    #             FROM project_task ps
    #             LEFT JOIN project_project pp ON ps.project_id = pp.id
    # 			LEFT JOIN  res_users aa ON pp.user_id = aa.id
    #         )
    #     """)

    project_name = fields.Char()
    employee = fields.Many2one('hr.employee')
    department = fields.Many2one('hr.department')
    planned_hour = fields.Float()
    worked_hour = fields.Float()
    assigned_from = fields.Char()
    assigned_to = fields.Char()

    def init(self):
        self._cr.execute(""" 
            CREATE OR REPLACE VIEW project_info_details AS ( 
                SELECT row_number() OVER () AS id,
                line.id AS line_id,
                line.member_id AS member_id,
				line.employee_id AS employee,
				emp.department_id AS department,
				line.planned_hour AS planned_hour,
				line.worked_hour AS worked_hour,
				line.assigned_from AS assigned_from,
				line.assigned_to AS assigned_to,
                pp.id AS project_id,
                pp.name AS project_name
				FROM member_information line
				LEFT JOIN hr_employee emp ON emp.id = line.employee_id
				LEFT JOIN hr_department dpt ON dpt.id = emp.department_id
				INNER JOIN project_project pp ON pp.id = line.member_id
            )
        """)
