# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PrimerModulo(models.Model):
	_name = 'primer.modulo'
	_description = 'Este es el primer modulo'

	name = fields.Char(string="Title", required=True)
	description = fields.Text()

	responsable_id = fields.Many2one('res.users',ondelete = 'set null', string='Responsable', index=True)
	prueba = fields.Char(string="Este campo es de una prueba")

class session(models.Model):
	_name = "course.session"
	_description = "Session of course"

	name = fields.Char(required=True)
	start_date = fields.Date()
	duration = fields.Float(digits=(6, 2), help="Duration in days")
	seats = fields.Integer(string="Number of seats")

	instructor_id = fields.Many2one('res.partner', string="Instructor")
	course_id = fields.Many2one('primer.modulo', ondelete='cascade', string="course", required=True)
