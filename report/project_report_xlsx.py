from odoo import models


class ProjectReportXlsx(models.AbstractModel):
    _name = 'report.engineers_management.report_project_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, projects):
        row, col = 1, 1
        sheet = workbook.add_worksheet("Project Report")

        for proj in projects:
            date_style = workbook.add_format({'align': 'left', 'text_wrap': True, 'num_format': 'dd-mm-yyyy'})
            head = workbook.add_format({'align': 'center', 'bold': True, 'font_size': '20px', 'border': 2})
            column_head = workbook.add_format({'align': 'center', 'bold': True})
            column_data = workbook.add_format({'align': 'left', 'bold': False})
            sheet.merge_range(row, col, row + 1, col + 3, "Project Details", head)
            row += 3
            bold = workbook.add_format({'bold': True})
            sheet.set_column('B:C', 30)
            sheet.write(row, col, "Project name: ", bold)
            sheet.write(row, col + 1, proj.name, bold)
            row += 1
            sheet.write(row, col, "Project ID: ", bold)
            sheet.write(row, col + 1, proj.project_id, bold)
            row += 1
            sheet.write(row, col, "Created on: ", bold)
            sheet.write(row, col + 1, proj.created_on, date_style)
            row += 1
            sheet.write(row, col, "Project Start Date: ", bold)
            sheet.write(row, col + 1, proj.project_start_date, date_style)
            row += 1
            sheet.write(row, col, "Project Close Date: ", bold)
            sheet.write(row, col + 1, proj.project_end_date, date_style)
            row += 2

            sheet.merge_range(row, col, row + 1, col + 6, "Employee Details", head)
            row += 3
            col = 1
            sheet.set_column('B:H', 20)
            sheet.write(row, col, "Employee Name", column_head)
            col += 1
            sheet.write(row, col, "Department", column_head)
            col += 1
            sheet.write(row, col, "Assigned From", column_head)
            col += 1
            sheet.write(row, col, "Assigned To", column_head)
            col += 1
            sheet.write(row, col, "Role", column_head)
            col += 1
            sheet.write(row, col, "Planned Hour", column_head)
            col += 1
            sheet.write(row, col, "Worked Hour", column_head)
            col = 1

            for line in proj.members_ids:
                row += 1
                sheet.write(row, col + 0, line.employee_id.name, column_data)
                sheet.write(row, col + 1, line.department_id.name, column_data)
                sheet.write(row, col + 2, line.assigned_from, date_style)
                sheet.write(row, col + 3, line.assigned_to, date_style)
                sheet.write(row, col + 4, line.role_id.name, column_data)
                sheet.write(row, col + 5, line.planned_hour, column_data)
                sheet.write(row, col + 6, line.worked_hour, column_data)
            row += 2
