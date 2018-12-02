import requests


hitbtc_base_url = 'https://api.hitbtc.com/api/2'
api_kei = '4bf0ef13bdada74384be1d3a0c9faab2'
secret = '1a8ddbadbdcbd91824d7222b03a4af3e'


#                   PUBLIC ENDPOINTS


def hitbtc_all_symbols():
    hitbtc_base_url = 'https://api.hitbtc.com/api/2'
    endpoint  = '/public/ticker'
    symbol = requests.get(hitbtc_base_url+endpoint)
    symbol = symbol.json()
    return symbol

def hitbtc_pair_data(pair):
    hitbtc_base_url = 'https://api.hitbtc.com/api/2'
    endpoint = '/public/ticker/'
    symbol = requests.get(hitbtc_base_url + endpoint + pair)
    symbol = symbol.json()
    return symbol


#                PRIVATE ENDPOINTS
#        authentication
def balance(publickey, secretkey):
    url = 'https://api.hitbtc.com/api/2/trading/balance'
    session = requests.Session()
    session.auth = (publickey, secretkey)
    result = session.get(url).json()

    return result


def order(publickey, secretkey, symbol, side, quantity, clientoid=None, type='market'):
    symbol = str(symbol)
    symbol = symbol.lower()
    if clientoid is None:
        orderData = {'symbol': symbol, 'side': side, quantity: str(quantity)}
    else:
        orderData = {'symbol': symbol, 'side': side, quantity: str(quantity), 'clientOrderId': clientoid}
    session = requests.session()
    session.auth = (publickey, secretkey)
    r = session.post('https://api.hitbtc.com/api/2/order', data=orderData).json()
    return r



def tradingfees(publickey, secretkey, symbol):
    url = 'https://api.hitbtc.com/api/2/trading/fee/'+symbol
    session = requests.session()
    session.auth = (publickey, secretkey)
    r = session.get(url).json()
    return r['takeLiquidityRate']


