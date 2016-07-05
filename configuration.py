#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
from trytond.pyson import Eval, Bool
from trytond.pool import Pool, PoolMeta

__all__ = ['Configuration']

class Configuration():
    __metaclass__ = PoolMeta
    __name__ = 'purchase.configuration'

    warehouse = fields.Property(fields.Many2One('stock.location', 'Warehouse',
        domain=[('type', '=', 'warehouse')]))
