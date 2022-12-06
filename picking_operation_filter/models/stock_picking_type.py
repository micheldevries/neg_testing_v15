from odoo import api, fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    active_operation = fields.Boolean(compute='_compute_hide_operation', store=True)
    update_dummy = fields.Boolean(string="Update Dummy field", default=False)

    @api.depends('count_picking', 'count_picking_ready', 'count_picking_late', 'update_dummy')
    def _compute_hide_operation(self):
        get_all_picking = self.search([])
        for record in get_all_picking:
            pic_ids = self.env['stock.picking'].search([('state', 'not in', ('done', 'cancel'))])
            mo_ids = self.env['mrp.production'].search([('state', 'not in', ('done', 'cancel'))])
            record.active_operation = False
            if pic_ids:
                if record.count_picking_draft > 0:
                    record.active_operation = True
                elif record.count_picking_ready > 0:
                    record.active_operation = True
                elif record.count_picking_waiting > 0:
                    record.active_operation = True
                elif record.count_picking_late > 0:
                    record.active_operation = True
                else:
                    record.active_operation = False
            if mo_ids:
                if record.count_picking_draft > 0:
                    record.active_operation = True
                elif record.count_picking_ready > 0:
                    record.active_operation = True
                elif record.count_picking_waiting > 0:
                    record.active_operation = True
                elif record.count_picking_late > 0:
                    record.active_operation = True
                else:
                    record.active_operation = False


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self, vals):
        res = super(StockPicking, self).create(vals)
        if res.picking_type_id:
            res.picking_type_id.write({'update_dummy': True})
        return res

    def write(self, vals):
        res = super(StockPicking, self).write(vals)
        if self.picking_type_id:
            self.picking_type_id.write({'update_dummy': True})
        return res
