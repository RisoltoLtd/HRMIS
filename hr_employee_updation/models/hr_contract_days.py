from odoo.exceptions import Warning
from odoo import models, fields, api, _


class HrEmployeeContract(models.Model):
    _inherit = 'hr.contract'

    def _get_default_notice_days(self):
        if self.env['ir.config_parameter'].get_param(
                'hr_resignation.notice_period'):
            return self.env['ir.config_parameter'].get_param(
                            'hr_resignation.no_of_days')
        else:
            return 0

    notice_days = fields.Integer(string="Notice Period", default=_get_default_notice_days)
    state = fields.Selection([
        ('draft', 'New'),
        ('open', 'Running'),
        ('close', 'Resigned'),
        ('cancel', 'Terminated')
    ], string='Status', group_expand='_expand_states', copy=False,
       tracking=True, help='Status of the contract', default='draft')
