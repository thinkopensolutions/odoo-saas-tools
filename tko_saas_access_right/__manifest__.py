# *- c0d1ng: u7f-8 -*-
# OpenERP, Open Source Management Solution
# Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be&gt;).
# Thinkopen - Brasil
# Copyright (C) Thinkopen Solutions (<http://www.thinkopensolutions.com.br&gt;)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    'name': 'TKO SaaS Access Rights',
    'category': 'SaaS',
    'summary': 'Add additional access rights to SaaS module',
    'website': 'http://tko.tko-uk.com/',
    "license": "AGPL-3", 
    'author' : 'TKO',
    'version': '10.0.0.0.0',
    'depends': ['saas_portal'],
    'data': [
        'security/ir.model.access.csv',
             ],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
