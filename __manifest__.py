# -*- coding: utf-8 -*-
{
    'name': 'Shokale Templates',
    'summary': """
        - Reporte persanalizado para la orden de venta y cotización
    """,
    'author': 'jcollado@tagre.pe',
    'version': '17.0',
    'website': 'http://www.tagre.pe',
    'category': 'sale',
    'depends': ['base', 'professional_templates'],
    "data": [
        "report/order_lines.xml",
        "report/sale_order_shokale_template_report.xml",
        "report/company_footer.xml",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml"
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
