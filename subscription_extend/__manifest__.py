##############################################################################
#
#    Author: Cravit.
#    Copyright 2017 B-informed B.V.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Subscription Extend",
    "summary": "Subscription Extend",
    "description": """
Subscription Extendr
    """,
    "website": "https://www.cravit.nl",
    'version': "15.0.1.0.0",
    "author": "Cravit",
    "license": "OPL-1",
    'category': 'Subscription',
    "depends": [
        'sale_subscription','account'
    ],
    "qweb": [],
    'data': [
        'views/sale_subscription_inh_view.xml',
        'report/invoice_subs_report_template.xml'
    ]
}
