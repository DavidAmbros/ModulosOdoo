# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalDiagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = "Diagnostico para los pacientes"
    _rec_name = 'id'
    paciente = fields.Many2one('hospital.paciente', string="Paciente",)
    medico = fields.Many2one('hospital.medico',string='Medico',)
    diagnostico = fields.Char("Diagnostico")