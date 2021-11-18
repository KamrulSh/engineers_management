# -*- coding: utf-8 -*-
{
    'name': "engineers_management",
    'sequence': 1,
    'summary': """
        To create engineers profile based on skills, assigned in the project and generate monthly invoices""",

    'description': """
        To create engineers profile based on skills, assigned in the project and generate monthly invoices
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'hr'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/engineer_view.xml',
        'views/engineer_position_view.xml',
        'views/technical_category_view.xml',
        'views/technical_technology_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
