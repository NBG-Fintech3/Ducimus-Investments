import requests
import hmac
import base64
import json
import time


#                       DATA
api_key = ''
passphrase = ''
secret = ''

okex_margin = ['eth_btc', 'bch_usdt', 'ltc_btc', 'etc_btc', 'eth_usdt','btc_usdt', 'ltc_usdt', 'etc_usdt',
               'qtun_btc', 'xrp_btc', 'xrp_usdt', 'eos_usdt', 'eos_btc', 'iost_btc']

CONTENT_TYPE = 'Content-Type'
OK_ACCESS_KEY = 'OK-ACCESS-KEY'
OK_ACCESS_SIGN = 'OK-ACCESS-SIGN'
OK_ACCESS_TIMESTAMP = 'OK-ACCESS-TIMESTAMP'
OK_ACCESS_PASSPHRASE = 'OK-ACCESS-PASSPHRASE'
APPLICATION_JSON = 'application/json'


#                       PUBLIC ENDPOINTS


def okex_all_symbols():
    symbols_url = 'https://www.okex.com/api/v1/tickers.do'
    symbol = requests.get(symbols_url)
    symbol = symbol.json()
    tickers = symbol['tickers']
    return tickers


def get_margin_tickers(tickers_list=okex_all_symbols(), okex_mar=okex_margin):
    marginList = []
    for ticker in tickers_list:
        if (ticker['symbol'] in okex_mar):
            marginList.append(ticker)
    return marginList


def okex_pair_data(pair):
    urlinfo = 'https://www.okex.com/api/v1/ticker.do'
    param = {'symbol':pair}
    pair_info = requests.get(urlinfo, params=param)
    pair_info = pair_info.json()
    ticker = pair_info['ticker']
    return ticker


def usrInfo(apiKey):
    try:
        url = 'https://www.okex.com/api/v1/userinfo.do'
        usrInfoData = {'api_key': apiKey}
        info = requests.post(url, data = usrInfoData)#,timeout=10)
        info = info.json()
        usd = info['info']['funds']['free']['usd']
        btc = info['info']['funds']['free']['btc']
        return usd, btc
    except:
        print('CANT GET MY FUNDS INFO')


def okex_server_time_UNIX():
    url = 'https://www.okex.com/api/general/v3/time'
    response = requests.get(url)
    response = response.json()
    return response['epoch']


def okex_server_time_ISO():
    url = 'https://www.okex.com/api/general/v3/time'
    response = requests.get(url)
    response = response.json()
    return response['iso']


#                       PRIVATE ENDPOINTS
#                        NEEDED FUNCTIONS


def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        url = url + str(key) + '=' + str(value) + '&'

    return url[0:-1]


def signature(timestamp, method, request_path, body=None, secret_key=None):
    if str(body) == '{}' or str(body) == 'None':
        body = ''
    message = str(timestamp) + str.upper(method) + request_path + str(body)
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)


def get_header(api_key, sign, timestamp, passphrase):
    header = dict()
    header[CONTENT_TYPE] = APPLICATION_JSON
    header[OK_ACCESS_KEY] = api_key
    header[OK_ACCESS_SIGN] = sign
    header[OK_ACCESS_TIMESTAMP] = str(timestamp)
    header[OK_ACCESS_PASSPHRASE] = passphrase
    return header


#TODO check transfer System
def tranfer(api_key, secret, passphrase, token, amount, from_account, to_account, instrument_id=None,
            request_path='/api/account/v3/transfer', method='POST', timestamp=None):
    if to_account == 'margin':
        if instrument_id is None:
            return 'Need a pair'
    accounts = {'sub account': 0,
               'spot': 1,
               'futures': 3,
               'C2C': 4,
               'margin': 5,
               'wallet': 6,
               'ETT': 7}
    parameters = {'currency': token, 'amount': amount, 'from': accounts[from_account], 'to': accounts[to_account],
                  'instrument_id': instrument_id}
    bodyCertificate = json.dumps(parameters)
    #    CREATING THE REQUESTS PATH
    request_path += parse_params_to_str(parameters)
    url = 'https://www.okex.com'
    url += request_path
    if timestamp is None:
        timestamp = okex_server_time_ISO()
    sign = signature(timestamp, method, request_path, body=str(bodyCertificate), secret_key=secret)
    header = get_header(api_key, sign, timestamp, passphrase)
    response = requests.post(url, data=bodyCertificate, headers=header)
    response = response.json()
    # TODO post client_oid,orderID,notional to sql_DB

    return response


#                      SPOT
def market_sell(pair, size, api_key, secret, passphrase, client_oid=None, type='market', side='sell', margin_trading=1,
                request_path='/api/spot/v3/orders', method='POST', timestamp=None):
    if client_oid is None:
        client_oid = ''
    #   JSON FOR THE PARAMETERS AND BODY
    parameters = {'client_oid': client_oid, 'type': type, 'side': side, 'instrument_id': pair,
                   'margin_trading': margin_trading, 'size': size}
    bodyCertificate = json.dumps(parameters)
    #    CREATING THE REQUESTS PATH
    request_path += parse_params_to_str(parameters)
    url = 'https://www.okex.com'
    url += request_path
    if timestamp is None:
        timestamp = okex_server_time_ISO()
    sign = signature(timestamp, method, request_path,body=str(bodyCertificate), secret_key=secret)
    header = get_header(api_key, sign, timestamp, passphrase)
    response = requests.post(url,data=bodyCertificate, headers=header)
    response = response.json()
    # TODO post client_oid,orderID,notional to sql_DB

    return response


def market_buy(pair, notional, api_key, secret, passphrase, client_oid=None, type='market',
               side='buy', margin_trading=1, request_path='/api/spot/v3/orders', method='POST', timestamp=None):
    if client_oid is None:
        client_oid = '20180728'
    #   JSON FOR THE PARAMETERS AND BODY
    parameters = {'client_oid': client_oid, 'type': type, 'side': side, 'instrument_id': pair,
                   'margin_trading': margin_trading, 'notional': notional}
    bodyCertificate = json.dumps(parameters)
    #    CREATING THE REQUESTS PATH
    request_path += parse_params_to_str(parameters)
    url = 'https://www.okex.com'
    url += request_path
    if timestamp is None:
        timestamp = okex_server_time_ISO()
    sign = signature(timestamp, method, request_path, body=str(bodyCertificate), secret_key=secret)
    header = get_header(api_key, sign, timestamp, passphrase)
    response = requests.post(url, data=bodyCertificate, headers=header)
    response = response.json()
    # TODO post client_oid,orderID,notional to sql_DB

    return response


def amount_currency(token, api_key, secret, passphrase, request_path='/api/spot/v3/accounts/',
                    method='GET',timestamp=None):
    request_path = request_path + token
    url = 'https://www.okex.com'
    if (timestamp == None):
        timestamp = okex_server_time_ISO()
    sign = signature(timestamp, method, request_path, body='', secret_key=secret)
    header = get_header(api_key, sign, timestamp, passphrase)
    response = requests.get(url+request_path,headers=header)
    response = response.json()
    return response

# TODO check what happenes when having X amount of btc and loaning x<X btc worth eth.
#  What are are the values on amount_currency()???


def order_details(api_key, secret, passphrase, order_id, instrument_id, method='GET',
                  request_path=' /api/margin/v3/orders/', timestamp=None):
    parameters = {'instrument_id': instrument_id}
    bodyCertificate = json.dumps(parameters)
    request_path += str(order_id)
    url = 'https://www.okex.com'
    if (timestamp == None):
        timestamp = okex_server_time_ISO()
    sign = signature(timestamp, method, request_path, body=str(bodyCertificate), secret_key=secret)
    header = get_header(api_key, sign, timestamp, passphrase)
    response = requests.get(url+request_path, headers=header)
    response = response.json()
    return response
    pass


#                    MARGIN
def get_loan(pair, currency, amount, api_key, secret, passphrase,
             timestamp=None, method='POST', request_path='/api/margin/v3/accounts/borrow'):
    parameters = {"instrument_id": pair, "currency": currency, "amount": amount}
    bodyCertificate = json.dumps(parameters)
    request_path += parse_params_to_str(parameters)
    url = 'https://www.okex.com' + request_path
    if timestamp is None:
        timestamp = okex_server_time_ISO()
    sign = signature(timestamp, method, request_path,body= str(bodyCertificate),secret_key= secret)
    header = get_header(api_key, sign, timestamp, passphrase)
    response = requests.post(url, data=bodyCertificate, headers=header)
    response = response.json()
    # TODO post borrow_id to sql_DB
    return response


def margin_info(api_key, secret, passphrase, request_path='/api/margin/v3/accounts', method='GET',timestamp=None):
    url = 'https://www.okex.com'
    if (timestamp == None):
        timestamp = okex_server_time_ISO()
    sign = signature(timestamp, method, request_path, body='', secret_key=secret)
    header = get_header(api_key, sign, timestamp, passphrase)
    response = requests.get(url + request_path, headers=header)
    response = response.json()
    return response


def repay(api_key, secret, passphrase, borrow_id, pair, currency, amount,
          request_path='/api/margin/v3/accounts/repayment', method='POST', timestamp=None):
    parameters = {"borrow_id": borrow_id, "instrument_id": pair, "currency": currency, "amount": amount}
    bodyCertificate = json.dumps(parameters)
    request_path += parse_params_to_str(parameters)
    url = 'https://www.okex.com' + request_path
    if timestamp is None:
        timestamp = okex_server_time_ISO()
    sign = signature(timestamp, method, request_path, body=str(bodyCertificate), secret_key=secret)
    header = get_header(api_key, sign, timestamp, passphrase)
    response = requests.post(url, data=bodyCertificate, headers=header)
    response = response.json()
    # TODO post borrow_id to sql_DB
    return response


def margin_market_order(api_key, secret, passphrase, pair, side, amount, type='market', margin_trading=2,
                        method='POST',client_oid=None, request_path='/api/margin/v3/orders', timestamp=None):
    if client_oid is None: client_oid = ''
    if side =='buy':
        parameters = {'client_oid': client_oid, 'type': type, 'side': side, 'instrument_id': pair,
                      'margin_trading': margin_trading, 'size': amount}
    elif side == 'sell':
        parameters = {'client_oid': client_oid, 'type': type, 'side': side, 'instrument_id': pair,
                      'margin_trading': margin_trading, 'size': amount}
        # TODO check if notional is needed
    else:
        raise('Chose a side')
    bodyCertificate = json.dumps(parameters)
    #    CREATING THE REQUESTS PATH
    request_path += parse_params_to_str(parameters)
    url = 'https://www.okex.com'
    url += request_path
    if timestamp is None:
        timestamp = okex_server_time_ISO()
    sign = signature(timestamp, method, request_path, body=str(bodyCertificate), secret_key=secret)
    header = get_header(api_key, sign, timestamp, passphrase)
    response = requests.post(url, data=bodyCertificate, headers=header)
    response = response.json()
    return response
    pass


# TODO not working
def loan_history(api_key, secret, passphrase, status=None, from_id=0, to_id=1, limit=100,
             timestamp=None, method='GET', request_path='/api/margin/v3/accounts/borrowed'):
    if status is None:
        status= 0
    parameters = {"status": status}#, 'from': from_id, 'to': to_id, 'limit':limit}
    bodyCertificate = json.dumps(parameters)
    request_path += parse_params_to_str(parameters)
    url = 'https://www.okex.com' + request_path
    if timestamp is None:
        timestamp = okex_server_time_ISO()
    sign = signature(timestamp, method, request_path,body= str(bodyCertificate),secret_key= secret)
    header = get_header(api_key, sign, timestamp, passphrase)
    response = requests.post(url, data=bodyCertificate, headers=header)
    response = response.json()
    # TODO post borrow_id to sql_DB
    return response



def sort(pair, amount, api_key, secret, passphrase):
    transfer_result = tranfer(api_key, secret, passphrase, token='btc', amount=str(1.01*amount), from_account='spot',
                         to_account='margin', instrument_id=pair)
    if transfer_result['result'] != 'true':
        return 0

