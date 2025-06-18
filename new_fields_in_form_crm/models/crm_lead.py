from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = "crm.lead"

    monto_usd_pws = fields.Integer(
        string="Monto USD PWS",
        tracking=True,
    )

    monto_usd_se = fields.Integer(
        string="Monto USD SE",
        tracking=True,
    )
    
    bu_id = fields.Many2one(
        "bu", 
        string="BU",
        tracking=True,
    )
    
    portafolio_id = fields.Many2one(
        "portafolio", 
        string="Portafolio",
        tracking=True,
    )
    
    project_management_id = fields.Many2one(
        "hr.employee", 
        string="Project Management",
        tracking=True,
    )
    
    gm_usd_esperado = fields.Integer(
        string="GM USD (Esperado)",
        tracking=True,
    )
    gm_usd_real = fields.Integer(
        string="GM USD (Real)",
        tracking=True,
    )
    incentivos_usd = fields.Integer(
        string="Incentivos USD",
        tracking=True,
    )
    costo_financiero_usd = fields.Integer(
        string="Costo financiero USD",
        tracking=True,
    )
    horas_hombre_usd = fields.Integer(
        string="Horas Hombre USD",
        tracking=True,
    )
    viaticos_usd = fields.Integer(
        string="Viaticos USD",
        tracking=True,
    )
    transporte_usd = fields.Integer(
        string="Transporte USD",
        tracking=True,
    )
    imprevistos_usd = fields.Integer(
        string="Imprevistos USD",
        tracking=True,
    )
    epp_usd = fields.Integer(
        string="EPP USD",
        tracking=True,
    )
    mtto_oficina_usd = fields.Integer(
        string="Mtto Oficina USD",
        tracking=True,
    )
    equipos_usd = fields.Integer(
        string="Equipos USD",
        tracking=True,
    )