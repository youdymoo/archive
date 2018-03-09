from anvil import *
import stripe.checkout
import anvil.users
import tables
from tables import app_tables
import anvil.server
from plotly import graph_objs as go
from EditStock import EditStock

class StockChart (StockChartTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    # Plot the stock price of the symbol stock
    prices = anvil.server.call('get_stock_price', self.item['symbol'])
    self.plot_1.data = go.Scatter(x=[p['date'] for p in prices],
                                  y=[p['close'] for p in prices],
                                  fill='tozeroy')
                              
                           

  def link_1_click (self, **event_args):
    # This method is called when the link is clicked
    open_form('HomePage')

  def button_1_click (self, **event_args):
    # This method is called when the button is clicked
    if confirm("Remove '%s' (%s) from your portfolio?" % (self.item['company_name'], self.item['symbol'])):
      anvil.server.call('remove_stock', self.item)
      open_form('HomePage')
      

  def button_2_click (self, **event_args):
    # This method is called when the button is clicked
    es = EditStock(item=self.item)
    alert(es, title="Edit Stock")
    self.refresh_data_bindings()



