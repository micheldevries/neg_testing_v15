import logging

from odoo import SUPERUSER_ID, Command, _, api, fields, models

_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    customer_reference = fields.Char(string="Customer Reference")
    customer_id = fields.Many2one("res.partner", string="For Customer")

    def _prepare_invoice_data(self):
        vals = super(SaleSubscription, self)._prepare_invoice_data()
        if self.customer_reference:
            vals.update({
                'ref': self.customer_reference,
            })
        return vals
