from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    qty_reserved = fields.Float(string="Reserved", help="QTY of reserved items", compute='_compute_qty_reserved', digits='Product Unit of Measure',)

    @api.depends('qty_available_today')
    def _compute_qty_reserved(self):
        for line in self:
            if line.state in ['sale', 'done']:
                line.qty_reserved = line.qty_available_today
            else:
                line.qty_reserved = 0.0
