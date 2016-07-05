#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
import datetime
from decimal import Decimal
from trytond.model import Workflow, ModelView, ModelSQL, fields
from trytond import backend
from trytond.pool import Pool, PoolMeta

__all__ = ['Purchase']


class Purchase():
    __metaclass__ = PoolMeta
    __name__ = 'purchase.purchase'
    _rec_name = 'reference'

    @classmethod
    def default_warehouse(cls):
        pool = Pool()
        Config = pool.get('purchase.configuration')
        if Config(1).warehouse:
            w = Config(1).warehouse
            return w.id
        else:
            cls.raise_user_error("No ha configurado la bodega por defecto, dirijase a: \n Configuracion-Configuracion de Compras")


    @classmethod
    def __setup__(cls):
        super(Purchase, cls).__setup__()
