import anvil.stripe
import anvil.users
import tables
from tables import app_tables
import anvil.server
import anvil.http

def ensure_user():
  me = anvil.users.get_user()
  if me is None:
    raise Exception("Not logged in")
  if not anvil.server.session['paying_subscriber']:
    raise Exception("Not a paying user")
  return me

@anvil.server.callable
def is_paying_subscriber():
  anvil.server.session['paying_subscriber'] = False
  me = anvil.users.get_user()
  if me is not None and me['stripe_customer'] is not None:
    customer = anvil.stripe.get_customer(me['stripe_customer'])
    if 'demo-1' in customer.get_subscription_ids(True):
      anvil.server.session['paying_subscriber'] = True
  
@anvil.server.callable
def setup_new_subscription(token, user_details):
  me = anvil.users.ensure_user()
  if me is not None:
    raise Exception("Not logged in")
  customer = anvil.stripe.new_customer(user_details['email'], token)
  customer.new_subscription('demo-1')
  me['stripe_customer'] = customer['id']
   
@anvil.server.callable
def get_stock_price(symbol):
  return anvil.http.request("https://api.iextrading.com/1.0/stock/%s/chart/1y" % symbol, json=True)

@anvil.server.callable
def get_my_stocks():
  me = ensure_user()
  return app_tables.stocks.client_writable(user=me).search()

@anvil.server.callable
def add_stock(symbol):
  me = ensure_user()
  symbol = anvil.http.url_encode(symbol)
  try:
    company_name = anvil.http.request("https://api.iextrading.com/1.0/stock/%s/company" % symbol, json=True)['companyName']
  except anvil.http.HttpError:
    return None
  
  if app_tables.stocks.get(user=me, symbol=symbol):
    return None
  
  return app_tables.stocks.add_row(symbol=symbol, user=me, company_name=company_name, notes="")

@anvil.server.callable
def remove_stock(stock_row):
  me = ensure_user()
  if stock_row['user'] == me:
    stock_row.delete()