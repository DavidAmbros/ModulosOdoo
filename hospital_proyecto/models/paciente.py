# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalPaciente(models.Model):
    _name = 'hospital.paciente'
    _description = "pacientes"
    _rec_name = 'nombre'

    nombre = fields.Char("Nombre", required=True)
    apellidos = fields.Char("Apellidos")
    simptomas = fields.Char("Simptomas")