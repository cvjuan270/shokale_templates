# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ResParter(models.Model):
    _inherit = 'res.partner'


    custom_contact = fields.Char(string='Contacto')
    