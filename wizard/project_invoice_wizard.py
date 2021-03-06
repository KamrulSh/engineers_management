from odoo import models, fields, api, _


class ProjectDashboard(models.TransientModel):
    _name = 'project.invoice.wizard'

    project_id = fields.Many2one('project.project', string="Project name")
    employee_id = fields.Many2one('hr.employee', string="Employee name")
    invoices = fields.Html("Report invoices")

    def invoices_query(self):
        # print(self.project_id.name, self.employee_id.name)
        select = f"""
                    SELECT row_number() OVER () AS id,
                    line.move_id AS line_id,
                    line.move_name AS invoice_name,
        			res.name AS customer,
        			move.invoice_date AS invoice_date,
                    emp.name AS employee_name,
        			line.quantity AS quantity,
                    line.price_unit AS price_unit
                    FROM account_move_line line
                    LEFT JOIN account_move move ON move.id = line.move_id
        			LEFT JOIN res_partner res ON res.id = move.commercial_partner_id
                    INNER JOIN hr_employee emp ON emp.id = line.project_employee_id"""

        where = f"""
                    WHERE move.project_id = {self.project_id.id}
                    """
        whereAnd = f"""
                    AND line.project_employee_id = {self.employee_id.id}
                    """
        orderby = f"""
                    ORDER BY invoice_name
                    """

        if self.project_id and self.employee_id:
            self._cr.execute(select + where + whereAnd + orderby)
        elif self.project_id:
            self._cr.execute(select + where + orderby)
        else:
            self._cr.execute(select + orderby)

        invoices_data = self._cr.dictfetchall()
        return invoices_data

    @api.onchange('project_id')
    def _onchange_project(self):
        if self.project_id:
            emp_ids = self.env['member.information'].search([('member_id', '=', self.project_id.id)])
            # print(emp_ids, emp_ids.employee_id.ids)

            if self.employee_id and self.employee_id.id in emp_ids.employee_id.ids:
                pass
            else:
                self.employee_id = False

            res = {'domain': {'employee_id': [('id', 'in', emp_ids.employee_id.ids)]}}
            return res

    @api.onchange("project_id", "employee_id")
    def action_preview_report(self):

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
                    <tr style="text-align: center;">
                        {th}
                    </tr>
                """
        th = """<th>{}</th>\n"""
        td = """<td>{}</td>\n"""
        tr = """<tr>{}</tr>\n"""

        head = ''
        body = ''
        column_header = ['Invoice ID', 'Invoice Date', 'Customer Name', 'Engineer Name', 'Quantity', 'Price']
        head += thead.format(th="".join(map(th.format, column_header)))

        invoices_data = self.invoices_query()

        for i in range(0, len(invoices_data)):
            column_value = [invoices_data[i]['invoice_name'],
                            invoices_data[i]['invoice_date'],
                            invoices_data[i]['customer'],
                            invoices_data[i]['employee_name'],
                            invoices_data[i]['quantity'],
                            invoices_data[i]['price_unit']]
            body += tr.format("".join(map(td.format, column_value)))
        view_invoices = table.format(thead=head, tbody=body)
        self.write({'invoices': view_invoices})

    def action_print_report(self):
        self.action_preview_report()
        invoices_data = self.invoices_query()
        data = {
            'form_data': self.read()[0],
            'invoices_data': invoices_data
        }
        return self.env.ref('engineers_management.action_invoice_wizard').report_action(self, data=data)

    def action_print_report_xlsx(self):
        self.action_preview_report()
        invoices_data = self.invoices_query()
        data = {
            'form_data': self.read()[0],
            'invoices_data': invoices_data
        }
        return self.env.ref('engineers_management.action_report_project_invoices').report_action(self, data=data)
