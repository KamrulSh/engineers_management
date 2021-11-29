from odoo import models, fields, api


class InvoiceInformation(models.Model):
    _inherit = 'account.move'
    _description = 'Invoice Information'

    project_id = fields.Many2one('project.project', string='Project name')

    @api.onchange("project_id")
    def _onchange_engineer(self):
        for record in self:
            lines = [(5, 0, 0)]
            for line in record.project_id.members_ids:
                val = {
                    'engineer_id': line.name,
                    'name': line.role.id,
                }
                lines.append((0, 0, val))
            record.invoice_line_ids = lines


class InvoiceLineInformation(models.Model):
    _inherit = 'account.move.line'
    _description = 'Invoice Line Information'

    engineer_id = fields.Many2one('hr.employee', string='Engineer name', readonly=True)
