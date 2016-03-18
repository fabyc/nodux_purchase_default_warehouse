# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool
from .configuration import *
from .purchase import *

def register():
    Pool.register(
        Configuration,
        Purchase,
        module='nodux_purchase_default_warehouse', type_='model')
