from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    id = fields.Integer('id',required=True)
    continentorigen = fields.Char('contient_de_origen')
    datanaix = fields.Date('Data de naixament')
    paisorigen = fields.Char('pais_de_origen')
    sexe = fields.Char('sexe')