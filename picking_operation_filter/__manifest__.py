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
    "name": "Picking Operation Filter",
    "summary": "Picking Operation Filter",
    "description": """
Picking Operation Filter
    """,
    "website": "https://www.cravit.nl",
    'version': "15.0.1.0.0",
    "author": "Cravit",
    "license": "OPL-1",
    'category': 'Accounting',
    "depends": [
        'stock_barcode','stock'
    ],
    "qweb": [],
    'data': [
        'views/stock_picking_type.xml',
    ]
}
