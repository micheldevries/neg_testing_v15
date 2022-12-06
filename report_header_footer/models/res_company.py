# -*- coding: utf-8 -*-
from odoo import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    report_custom_header = fields.Binary(string="Header")
    report_custom_footer = fields.Binary(string="Footer")
