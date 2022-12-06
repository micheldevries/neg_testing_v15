from odoo import _, fields, models
from odoo.exceptions import ValidationError


class CollieLabelWizard(models.TransientModel):
    _name = 'collie.label.wizard'

    no_of_copy = fields.Integer(default=1)
    picking_id = fields.Many2one('stock.picking')

    def action_print_collie_labels(self):
        if self.no_of_copy > 0:
            self.picking_id = self._context.get('active_id')
            report_action = self.env.ref("report_extend.neg_print_collie_label_zpl_action").report_action(self)
            report_action['close_on_report_download'] = True
            return report_action
        else:
            raise ValidationError(_("You need to enter at least 1 no of copy"))
