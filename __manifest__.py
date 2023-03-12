# -*- coding: utf-8 -*-
{
    'name': "IK_Planner",

    'summary': """
    Modulo para la gestion de actividades
    """,

    'description': """
        Modulo creado para la asignatura de SXE
    """,

    'author': "a22ikeraa",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base' , 'calendar'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
