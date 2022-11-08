# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo para información'

    name = fields.Char(string="Título:")
    description = fields.Char(string="Descripción:")
