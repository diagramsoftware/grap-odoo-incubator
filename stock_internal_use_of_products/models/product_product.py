# coding: utf-8
# Copyright (C) 2013 - Today: GRAP (http://www.grap.coop)
# @author Julien WESTE
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _, api, models
from openerp.exceptions import Warning as UserError


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.multi
    def _get_expense_account(self):
        """ get the income and expense accounts related to product.
        @return: dictionary which contains information regarding
            income and expense accounts
        """
        self.ensure_one()
        categ = self.categ_id

        expense_account = (
            self.property_account_expense or (
                categ and categ.property_account_expense_categ or False))

        if not expense_account:
            raise UserError(_(
                "The product %s has not account expense defined. Please define"
                " one and try again") % (self.name))

        return {
            'account_expense': expense_account,
        }
