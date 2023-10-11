'''
rheology model collection
-----------------------------------
'''
__version__ = "0.1"

from .models import HB, TC, carreau, casson, Newtonian, cross, Powerlaw, Bingham
from .functions import library_to_table, library_to_renderjson, library