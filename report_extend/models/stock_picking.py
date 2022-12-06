from odoo import _, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    client_order_ref = fields.Char(string="Customer Reference")

    def action_open_collie_labels_wizard(self):
        return {
            'name': _('Enter No of copies'),
            'type': 'ir.actions.act_window',
            'res_model': 'collie.label.wizard',
            'view_mode': 'form',
            'target': 'new',
        }
