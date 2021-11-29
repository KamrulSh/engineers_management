from odoo import models, fields, api


class InvoiceInformation(models.Model):
    _inherit = 'account.move'
    _description = 'Invoice Information'

    project_id = fields.Many2one('project.project', string='Project name')

    @api.onchange("project_id")
    def _onchange_invoice_information(self):

        for record in self:
            account_id = self.env['account.account'].search([], limit=1)
            record.invoice_line_ids = False
            lines = []
            for line in record.project_id.members_ids:
                val = {
                    'engineer_id': line.name,
                    'name': line.name.id,
                    'account_id': account_id.id
                }
                lines.append((0, 0, val))
            record.invoice_line_ids = lines


class InvoiceLineInformation(models.Model):
    _inherit = 'account.move.line'
    _description = 'Invoice Line Information'

    engineer_id = fields.Many2one('hr.employee', string='Engineer name')
