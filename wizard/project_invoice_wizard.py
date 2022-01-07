from odoo import models, fields, api, _


class ProjectDashboard(models.TransientModel):
    _name = 'project.invoice.wizard'

    project_id = fields.Many2one('project.project', string="Project name", required=True)
    invoice_id = fields.Many2one('account.move', string="Invoice name")
    invoices = fields.Html("Report invoices")

    def action_print_report(self):
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

        project_id = self.project_id

        self._cr.execute(f""" 
--             CREATE OR REPLACE VIEW project_invoice_wizard AS ( 
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
            INNER JOIN hr_employee emp ON emp.id = line.project_employee_id
            WHERE move.project_id = {project_id.id}
            ORDER BY invoice_name
--             )
        """)
        invoices_data = self._cr.dictfetchall()

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

        data = {
            'form_data': self.read()[0],
            'invoices_data': invoices_data
        }
        return self.env.ref('engineers_management.action_invoice_wizard').report_action(self, data=data)
