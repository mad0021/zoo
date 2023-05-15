from odoo import models, fields     
class zoo_especie(models.Model): 
    _name = 'zoo.especie' 
    id = fields.Integer('id', required=True)     
    familia = fields.Char('familia')   
    nomcientific = fields.Char('nom_cientific') 
    nomvulgar = fields.Char('nom_vulgar') 
    perill = fields.Char('perill_extencio')