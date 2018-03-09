from anvil import *
import stripe.checkout
import anvil.server
import anvil.users
import tables
from tables import app_tables

class ItemTemplate1(ItemTemplate1Template):

  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def symbol_lnk_click (self, **event_args):
    # This method is called when the link is clicked
    open_form('StockChart', item=self.item)

