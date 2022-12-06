{
    'name': "Delivery Salesorder Report",

    'summary': """Delivery Salesorder Report""",
    'description': """Delivery Salesorder Report which prints related sales order from receipt in purchase orders
    and also calculates reserved quantity in sale order line
    """,
    'author': "Cravit",
    'website': "https://www.cravit.nl",
    'license': "OPL-1",
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': ['base', 'stock', 'sale', 'sale_stock'],
    'data': [
        'views/stock_picking_view.xml',
        'views/sale_order_view.xml',
        'data/report_paperformat.xml',
        'views/report_related_so.xml',
    ],
}
