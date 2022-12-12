# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

##################
# TIPOS DE DATOS #
##################
# odoo.fields.Boolean
# odoo.fields.Char
# odoo.fields.Float
# odoo.fields.Integer

# odoo.fields.Binary
# odoo.fields.Html
# odoo.fields.Image
# odoo.fields.Monetary
# odoo.fields.Selection
# odoo.fields.Text
# odoo.fields.Date
# odoo.fields.DateTime

##################################
# CLASE DE DEFINICIÓN DE MODELO  #
##########################################################################################
# Cada modelo se crea en un fichero independiente en el paquete models.                  #
# Añadimos el modelo a la BD reiniciando el sistema.                                     #
# Enlazamos los atributos del modelo con las vistas a través de sus nombres de variable. #
##########################################################################################
class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo para información'
    _sql_constraints = [('name', 'unique(name)', 'Non se pode repetir o nome')]  # restricciones de unicidad
    _order = "name asc"

    name = fields.Char(string="Título:")
    description = fields.Text(string="Descripción:")
    peso = fields.Float(string="Peso:", default=4.5)
    sexo_traducido = fields.Selection([('Mujer', 'Muller'), ('Hombre', 'Home'), ('Otros', 'Outros')], string='Sexo')
    autorizado = fields.Boolean(string="¿Autorizado?", default=True)
    literal = fields.Char(compute='_avisoAlto', string='Literal', store=False)
    alto_en_cm = fields.Integer(string="Alto en cm:")
    ancho_en_cm = fields.Integer(string="Ancho en cm:")
    longo_en_cm = fields.Integer(string="Longo en cm:")
    volume = fields.Float(compute="_volume", store=True, string="Volume en m3")
    densidade = fields.Float(compute="_densidade", store=True, string='Densidade en kg/m3')
    foto = fields.Binary(string='Foto')
    adxunto_nome = fields.Char(string="Nome Adxunto")
    adxunto = fields.Binary(string="Arquivo adxunto")

    @api.depends('alto_en_cm', 'longo_en_cm', 'ancho_en_cm')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = float(rexistro.alto_en_cm) * float(rexistro.longo_en_cm) * float(
                rexistro.ancho_en_cm) / 1000000

    @api.depends('peso', 'volume')
    def _densidade(self):
        for rexistro in self:
            try:
                rexistro.densidade = float(rexistro.peso) / float(rexistro.volume)
            except Exception as erro:
                rexistro.densidade = 0

    @api.onchange('alto_en_cm')
    def _avisoAlto(self):
        for rexistro in self:
            if rexistro.alto_en_cm > 7:
                rexistro.literal = 'O alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_en_cm
            else:
                rexistro.literal = ""

    @api.constrains('peso')  # Ao usar ValidationError temos que importar a libreria ValidationError
    def _constrain_peso(self):  # from odoo.exceptions import ValidationError
        for rexistro in self:
            if rexistro.peso < 1 or rexistro.peso > 10:
                raise ValidationError('Os peso de %s ten que ser entre 1 e 4 ' % rexistro.name)
