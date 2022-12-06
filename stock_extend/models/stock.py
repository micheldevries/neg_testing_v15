from odoo import api, fields, models
from odoo.tools import float_compare


class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    inventory_owner = fields.Many2one('res.partner', string='Inventory Owner', required=False,
                                      help="Link the contact from res.partner to the Consigment Warehouse")


class StockMove(models.Model):
    _inherit = "stock.move"

    def _prepare_move_line_vals(self, quantity=None, reserved_quant=None):
        res = super(StockMove, self)._prepare_move_line_vals(quantity, reserved_quant)
        if self.picking_id:
            res.update({'owner_id': self.picking_id.owner_id.id})
        else:
            if self.location_id and self.location_id.warehouse_id:
                res.update({'owner_id': self.location_id.warehouse_id.inventory_owner.id})
            else:
                if self.location_dest_id and self.location_dest_id.warehouse_id:
                    res.update({'owner_id': self.location_dest_id.warehouse_id.inventory_owner.id})
        return res


class StockPicking(models.Model):
    _inherit = "stock.picking"

    consignment_loc = fields.Boolean(related='location_dest_id.consignment_loc', store=True)
    validate_btn_visibility = fields.Boolean(compute='_compute_validate_btn_visibility', string="Validate Button", store=True)

    @api.depends('state', 'consignment_loc', 'location_dest_id')
    def _compute_validate_btn_visibility(self):
        for rec in self:
            if (rec.state in ('waiting', 'confirmed') or rec.show_validate == False) and rec.consignment_loc:
                rec.validate_btn_visibility = False
            elif rec.state == 'done':
                rec.validate_btn_visibility = False
            elif rec.consignment_loc and rec.show_validate:
                rec.validate_btn_visibility = False
            else:
                rec.validate_btn_visibility = True

    @api.model
    def create(self, vals):
        res = super(StockPicking, self).create(vals)
        if res.picking_type_id.code == 'incoming' and res.location_dest_id.warehouse_id:
            res.owner_id = res.location_dest_id.warehouse_id.inventory_owner.id
        if res.picking_type_id.code in ('outgoing', 'internal') and res.location_id.warehouse_id:
            res.owner_id = res.location_id.warehouse_id.inventory_owner.id
        return res

    @api.onchange('location_id', 'location_dest_id')
    def change_location_dest_location(self):
        if self.picking_type_id.code == 'incoming' and self.location_dest_id.warehouse_id:
            self.owner_id = self.location_dest_id.warehouse_id.inventory_owner.id
        if self.picking_type_id.code in ('outgoing', 'internal') and self.location_id.warehouse_id:
            self.owner_id = self.location_id.warehouse_id.inventory_owner.id

    def neg_validate_picking(self):
        sale_id = self.env['sale.order'].search([('name', '=', self.origin)], limit=1)
        pick_ids = self.search([('origin', '=', sale_id.name)])
        for picking in pick_ids:
            picking.action_assign()
            for move in picking.move_lines.filtered(
                lambda m: m.state not in ["done", "cancel"]
            ):
                rounding = move.product_id.uom_id.rounding
                if (
                    float_compare(
                        move.quantity_done,
                        move.product_qty,
                        precision_rounding=rounding,
                    )
                    == -1
                ):
                    for move_line in move.move_line_ids:
                        move_line.qty_done = move_line.product_uom_qty
            picking.with_context(skip_immediate=True, skip_sms=True).button_validate()
        return True


class StockQuant(models.Model):
    _inherit = "stock.quant"

    @api.onchange('location_id')
    def change_quant_location(self):
        if self.location_id and self.location_id.warehouse_id:
            self.owner_id = self.location_id.warehouse_id.inventory_owner.id


class StockScrap(models.Model):
    _inherit = "stock.scrap"

    @api.onchange('location_id')
    def change_scrap_location(self):
        if self.location_id and self.location_id.warehouse_id:
            self.owner_id = self.location_id.warehouse_id.inventory_owner.id


class StockLocation(models.Model):
    _inherit = "stock.location"

    consignment_loc = fields.Boolean(string="Consignment Location")
