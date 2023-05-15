from odoo import models, fields     
class zoo_zoo(models.Model): 
    _name = 'zoo.zoo'
    id =  fields.Integer('id', required=True) 
    grandaria = fields.Char('grandaria')     
    nom = fields.Char('nom')     
    ciutat = fields.Char('ciutat')
    pais = fields.Char('pais')