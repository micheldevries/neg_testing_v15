from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    client_order_ref = fields.Char(string='Customer Reference', size=20, copy=False)

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for picking in self.picking_ids:
            if self.client_order_ref:
                picking.client_order_ref = self.client_order_ref
        return res
