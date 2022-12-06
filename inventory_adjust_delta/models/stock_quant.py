# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class StockQuant(models.Model):
    _inherit = "stock.quant"

    qty_delta = fields.Integer(string="Qty Delta")

    @api.onchange('qty_delta')
    def qty_delta_update(self):
        if self.qty_delta:
            self.inventory_quantity = self.qty_delta + self.quantity
            
    @api.model
    def _get_inventory_fields_create(self):
        """ Returns a list of fields user can edit when he want to create a quant in `inventory_mode`.
        """
        res = super()._get_inventory_fields_create()
        res += ['qty_delta']
        return res

    @api.model
    def _get_inventory_fields_write(self):
        """ Returns a list of fields user can edit when he want to edit a quant in `inventory_mode`.
        """
        res = super()._get_inventory_fields_write()
        res += ['qty_delta']
        return res

    def inventory_quantity_update(self, qty_delta):
        self.inventory_quantity = qty_delta + self.quantity
        self.action_apply_inventory()
        self.write({'qty_delta': 0})
        return True

    def action_apply_inventory(self):
        super(StockQuant, self).action_apply_inventory()
        self.write({'qty_delta': 0})
