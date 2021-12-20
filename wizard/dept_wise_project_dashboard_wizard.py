from odoo import models, fields, api, _


class ProjectDashboard(models.TransientModel):
    _name = 'project.dashboard.wizard'

    department_id = fields.Many2one('hr.department', string="Department name", required=True)
    dashboard = fields.Html("Report dashboard")

    def project_dashboard_line_generate(self):
        cr = self._cr
        cr.execute("""select department_id, hr_department.name,count(*) 
                    from project_project join hr_department on hr_department.id=project_project.department_id 
                    group by project_project.department_id,hr_department.name""")
        fetch_data = cr.fetchall()
        data = []
        for i in range(0, len(fetch_data)):
            data.append([fetch_data[i][1], fetch_data[i][2]])

        table = """
                <table border="1" class="o_list_view table table-condensed table-striped o_list_view_ungrouped">
                    <thead>
                        {thead}
                    </thead>
                    <tbody>
                        {tbody}
                    </tbody>
                </table>
                """

        thead = """
                    <tr style="text-align: right;">
                        {th}
                    </tr>
                """
        th = """<th>{}</th>\n"""
        td = """<td>{}</td>\n"""
        tr = """<tr>{}</tr>\n"""

        head = ''
        body = ''
        column_header = ['Department', 'Project']
        head += thead.format(th="".join(map(th.format, column_header)))
        body += tr.format("".join(map(td.format, data[0], data[1])))

        view_dashboard = table.format(thead=head, tbody=body)
        self.write({'dashboard': view_dashboard})
