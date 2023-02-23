# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalMedico(models.Model):
    _name = 'hospital.medico'
    _description = "medicos"
    _rec_name = 'nombre'

    nombre = fields.Char("Nombre", required=True)
    apellidos = fields.Char("Apellidos")
    numero = fields.Char("Numero")