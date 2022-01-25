from odoo import models


class ProjectInvoiceReportXlsx(models.AbstractModel):
    _name = 'report.engineers_management.report_project_invoices_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, invoices):
        row, col = 1, 1
        sheet = workbook.add_worksheet("Invoice Report")
        invoices_data = data['invoices_data']
        form_data = data['form_data']
        date_style = workbook.add_format({'align': 'left', 'text_wrap': True, 'num_format': 'dd-mm-yyyy'})
        head = workbook.add_format({'align': 'center', 'bold': True, 'font_size': '20px', 'border': 2})
        column_head = workbook.add_format({'align': 'center', 'bold': True})
        column_data = workbook.add_format({'align': 'left', 'bold': False})
        total_row = workbook.add_format({'align': 'right', 'bold': True})
        bold = workbook.add_format({'bold': True})
        sheet.set_column('B:C', 30)
        sheet.write(row, col, "Project name: ", bold)
        if not form_data['project_id']:
            sheet.write(row, col + 1, "All projects invoices", bold)
        else:
            sheet.write(row, col + 1, form_data['project_id'][1], bold)
        row += 3

        sheet.merge_range(row, col, row + 1, col + 5, "Invoice Details", head)
        row += 3
        col = 1
        sheet.set_column('B:G', 20)
        sheet.write(row, col, "Invoice ID", column_head)
        col += 1
        sheet.write(row, col, "Invoice Date", column_head)
        col += 1
        sheet.write(row, col, "Customer Name", column_head)
        col += 1
        sheet.write(row, col, "Engineer name", column_head)
        col += 1
        sheet.write(row, col, "Quantity", column_head)
        col += 1
        sheet.write(row, col, "Price unit", column_head)
        col = 1

        total_price = 0
        for line in invoices_data:
            row += 1
            sheet.write(row, col + 0, line['invoice_name'], column_data)
            sheet.write(row, col + 1, line['invoice_date'], date_style)
            sheet.write(row, col + 2, line['customer'], column_data)
            sheet.write(row, col + 3, line['employee_name'], column_data)
            sheet.write(row, col + 4, line['quantity'])
            sheet.write(row, col + 5, line['price_unit'])
            total_price += line['price_unit']
        row += 2
        sheet.merge_range(row, col, row + 1, col + 3, "Total price=", total_row)
        sheet.merge_range(row, col + 4, row + 1, col + 5, total_price, total_row)
