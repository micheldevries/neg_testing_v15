from odoo import _, fields, models
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    related_sales_orders_ids = fields.Many2many(
        "sale.order", string="All related Sales Orders", help="All related SO’s for this PO"
    )
    related_so_count = fields.Integer(
        "Number of Sale Order's", compute="_compute_related_sale_order_count"
    )

    def _compute_related_sale_order_count(self):
        for so in self:
            sale_order = so.env["sale.order"].search(
                [("id", "in", self.related_sales_orders_ids.ids)]
            )
            so.related_so_count = len(sale_order)

    def action_popup_all_related_so(self):
        if self.related_sales_orders_ids:
            return self.env.ref(
                "delivery_salesorder_report.action_neg_print_all_related_so"
            ).report_action(self)
        else:
            raise UserError(_("Do not have any related Sales order"))

    def action_view_related_so(self):
        return {
            "name": _("Related Sales Order"),
            "type": "ir.actions.act_window",
            "res_model": "sale.order",
            "view_mode": "tree,form",
            "target": "current",
            "domain": [("id", "in", self.related_sales_orders_ids.ids)],
        }


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _prepare_picking(self):
        res = super(PurchaseOrder, self)._prepare_picking()
        vals = {
            "related_sales_orders_ids": [(6, 0, self._get_sale_orders().ids)],
        }
        res.update(vals)
        return res
