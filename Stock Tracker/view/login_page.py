from anvil import *
import stripe.checkout
import anvil.server
import anvil.users
import tables
from tables import app_tables

class LoginPage (LoginPageTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def form_show (self, **event_args):
    # This method is called when the HTML panel is shown on the screen
    while not anvil.users.get_user():
      anvil.users.login_with_form()
      
    if anvil.server.call('is_paying_subscriber'):
      open_form('HomePage')
    else:
      self.payment_pnl.visible = True

  def pay_btn_click (self, **event_args):
    # This method is called when the button is clicked
    token, user_details = stripe.checkout.get_token(amount=5000, currency="USD", title="Stock Tracker subscription")
    anvil.server.call('setup_new_subscription', token, user_details)
    open_form('HomePage')




