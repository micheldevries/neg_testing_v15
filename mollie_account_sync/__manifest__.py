# -*- coding: utf-8 -*-

{
    'name': 'Mollie Settlement Sync',
    'version': '15.0.0.1',
    'description': '',
    'summary': 'This module sync settlements from mollie',
    'author': 'Mollie',
    'maintainer': 'Applix',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'account_accountant'
    ],
    'data': [
        'views/account_journal.xml',
        'views/bank_statement.xml',
        'wizard/mollie_init_views.xml',
        'security/ir.model.access.csv'
    ],

    'images': [
        'static/description/cover.png',
    ],

    'assets': {
        'web.assets_qweb': [
            'mollie_account_sync/static/src/xml/*.xml'
        ],
        'web.assets_backend': [
            'mollie_account_sync/static/src/js/info_widget.js'
        ]
    },
}
