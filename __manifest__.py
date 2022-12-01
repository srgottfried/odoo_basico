# -*- coding: utf-8 -*-
{
    'name': "odoo_basico",

    'summary': """
        Proxecto 2""",

    'description': """
        Descripción do proxecto 2
    """,

    'author': "Eu",
    'website': "https://www.edu.xunta.gal/centros/iesteis",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # engadir models
        'views/suceso.xml',
        'views/informacion.xml',
        'views/templates.xml',

        # --------------------
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
