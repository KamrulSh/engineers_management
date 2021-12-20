# -*- coding: utf-8 -*-
{
    'name': "Engineers management",
    'sequence': 200,
    'summary': """
        Generate invoice for project""",

    'description': """
        To create engineers profile based on skills, assigned in the project and generate monthly invoices
    """,

    'author': "Niazi & Kamrul",
    'website': "https://www.bjitgroup.com",
    'category': 'Accounting',
    'version': '0.1',
    'depends': ['base', 'hr', 'project', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/engineer_view.xml',
        'views/technical_category_view.xml',
        'views/technical_technology_view.xml',
        'views/technical_skill_view.xml',
        'views/project_view.xml',
        'views/member_info_view.xml',
        'views/invoice_view.xml',
        'views/dashboard_views.xml',
        'wizard/dept_wise_project_dashboard_wizard.xml',
    ],
    'qweb': ['static/src/xml/dashboard.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
