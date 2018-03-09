from anvil import *
import stripe.checkout
import anvil.server
import anvil.users
import tables
from tables import app_tables

class HomePage (HomePageTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.stock_rpt.items = anvil.server.call('get_my_stocks')

  def button_1_click (self, **event_args):
    # This method is called when the button is clicked
    stock_row = anvil.server.call('add_stock', self.new_symbol_stock.text)
    if stock_row is None:
      alert("'%s' is an invalid stock, or you already have it in your portfolio" % self.new_symbol_stock.text)
      self.new_symbol_stock.text=''
      return
    self.new_symbol_stock.text=''
    open_form('StockChart', item=stock_row)

