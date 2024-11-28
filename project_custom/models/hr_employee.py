from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    id_card = fields.Binary(string="Copia de la tarjeta de identificación")
    driving_license = fields.Binary(string="Licencia para conducir")
    
    
    