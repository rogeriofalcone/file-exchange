# -*- coding: utf-8 -*-
###############################################################################
#
#   file_buffer for OpenERP
#   Authors: Sebastien Beau <sebastien.beau@akretion.com>
#            Benoît Guillot <benoit.guillot@akretion.com>
#   Copyright 2013 Akretion
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'file_buffer',
    'version': '1.0',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description': """
Definition : an abstract module that add a file protocole on the external referential.
It use in base_sale_multichannel to send the invoice, the rma report.
Also it's used in file_exchange
""",
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': ['abstract_automatic_task',
                ],
    'demo': [],
    'data': [
        'file_buffer_view.xml',
        'file_buffer_data.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'active': False,
}
