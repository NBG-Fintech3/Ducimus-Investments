from okex import *


print(amount_currency('BTC',api_key,secret,passphrase))

amount = 0.00052062
api  = api_key
passph = passphrase
sec = secret
data_pair = 'eth_btc'
pair = 'eth-btc'



#transfer_result = tranfer(api, secret, passph, token='btc', amount=str(1.01*amount), from_account='spot',
#                          to_account='margin', instrument_id=pair)
#print('TRANSFER', transfer_result)
#TODO check transfer_result['result'] to be true

# TODO check where to put 1.01
data = okex_pair_data(pair=data_pair)['sell']
borrowing_amount = 2* amount / float(data)
borrow_result = get_loan(pair=pair,currency='btc', amount=borrowing_amount,api_key=api,secret=sec,passphrase=passph)
# TODO         FROM borrow_result check if ['result']==True and hold borrow_id in database or variable
print('BORROW ', borrow_result)

#      SELL BORROWING AMOUNT
sell_result = margin_market_order(api_key=api,secret=sec,passphrase=passph, pair=pair, side='sell',
                                  amount=borrowing_amount)
print('SELL ', sell_result)
# TODO check sell_result['result'] == true

