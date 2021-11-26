from odoo import models, fields, api


class InvoiceInformation(models.Model):
    _inherit = 'account.move'
    _description = 'Invoice Information'

    project_id = fields.Many2one('project.project', string='Project name')
    engineer_id = fields.Many2one('hr.employee', string='Engineer name')

    # @api.onchange("project_id")
    # def _onchange_engineer(self):
    #     for record in self:
    #         print("============>", record.project_id.members_ids)
    #         # lines = [(5, 0, 0)]
    #         lines = []
    #         for line in record.project_id.members_ids:
    #             val = {
    #                 'member_id': line.id,
    #                 'member_price': 213421
    #             }
    #             lines.append((0, 0, val))
    #         print("============>", lines)
    #         record.invoice_ids = lines


class InvoiceLineInformation(models.Model):
    _inherit = 'account.move.line'
    _description = 'Invoice Line Information'

    engineer_id = fields.Many2one('hr.employee', string='Engineer name')
