from odoo import models, fields, api
from datetime import datetime, timedelta


class ProjectTask(models.Model):
    _inherit = "project.task"

    # employee_id = fields.Many2one('hr.employee')
    related_product_id = fields.Many2one(
        "product.product", string="Producto"
    )
    folder_url = fields.Char(string="Carpeta")
    task_file = fields.Char(string="Archivo")
    due_date = fields.Date(
        string="Fecha Límite", default=lambda self: self._default_due_date()
    )
    nro_ot = fields.Char(string="Nro OT", index=True)
    end_date = fields.Date(string="Fecha de entrega")
    executor = fields.Many2many("hr.employee",
        string="Ejecutor",
    )

    @api.model
    def _default_due_date(self):
        return (datetime.now() + timedelta(days=30)).date()
