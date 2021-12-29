from odoo import models, fields, api


class ProjectTaskDetails(models.Model):
    _name = "project.task.details"
    _auto = False
    _rec_name = 'id'

    project = fields.Many2one('project.project')
    task = fields.Char(string='Task')
    manager = fields.Many2one('res.users')
    partner = fields.Many2one('res.partner', string='Customer')
    date_deadline = fields.Char(string='Task Deadline')

    def init(self):
        self._cr.execute(""" 
            CREATE OR REPLACE VIEW project_task_details AS ( 
                SELECT row_number() OVER () as id,
                ps.project_id as project,
                ps.name as task,
                ps.date_deadline as date_deadline,
                pp.partner_id as partner,
				pp.user_id as manager
                FROM project_task ps 
                LEFT JOIN project_project pp ON ps.project_id = pp.id
				LEFT JOIN  res_users aa ON pp.user_id = aa.id
            )
        """)
