from odoo import models, fields, api

class Bu(models.Model):
    _name = 'bu'
    _description = 'Bu'
    
    name = fields.Char(string='Nombre del Estado', required=True, tracking=True,)
    
    crm_line_ids = fields.One2many('crm.lead', 'bu_id', 'CRM Lines')