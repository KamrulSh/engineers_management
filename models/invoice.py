from odoo import models, fields, api


class InvoiceInformation(models.Model):
    _inherit = 'account.move'
    _description = 'Invoice Information'

    project_id = fields.Many2one('project.project', string='Project name')
    print('project_id', project_id)

    @api.onchange("project_id")
    def _onchange_project_name(self):
        account_id = self.env['account.account'].search([], limit=1)
        partner_id = self.env['project.project'].search([('id', '=', 1)], limit=1)
        self.invoice_line_ids = False
        lines = [(5, 0, 0)]
        for line in self.project_id.members_ids:
            val = {
                'project_employee_id': line.employee_id,
                'name': line.employee_id.id,
                'account_id': account_id.id,
            }
            lines.append((0, 0, val))
        self.invoice_line_ids = lines
        self.partner_id = partner_id.partner_id


class InvoiceLineInformation(models.Model):
    _inherit = 'account.move.line'
    _description = 'Invoice Line Information'

    project_employee_id = fields.Many2one('hr.employee', string='Engineer name')
