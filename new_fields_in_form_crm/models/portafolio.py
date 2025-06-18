from odoo import models, fields, api

class Portafolio(models.Model):
    _name = 'portafolio'
    _description = 'Portafolio'
    
    name = fields.Char(string='Nombre', required=True, tracking=True)
    
    crm_line_ids = fields.One2many('crm.lead', 'portafolio_id', 'CRM Lines')