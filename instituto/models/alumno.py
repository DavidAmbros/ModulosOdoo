# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CicleAlumno(models.Model):
    _name = 'cicle.alumno'
    _description = "alumnos"

    nombre = fields.Char("Nombre", required=True)
    apellidos = fields.Char("Apellidos")
    edad = fields.Char("edad")
    modulo = fields.Many2many('cicle.modulo','alumno',string='modulo')
