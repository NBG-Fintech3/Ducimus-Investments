from okex import tranfer,okex_pair_data,margin_market_order,get_loan
import time


# TODO get pair and amount
# TODO (get api_key, passphrase, secret_key)

api=passph=pair=amount=sec=''
amount = float(amount)/2


transfer_result = tranfer(api,secret,passph,token='BTC',amount=str(1.01*amount),from_account='spot',
                          to_account='margin',instrument_id=pair)

# TODO check transfer_result['result'] to be true

# TODO check where to put 1.01
data = okex_pair_data(pair=pair)['sell']
borrowing_amount = 2* amount / float(data)
#borrow_result = get_loan(pair=pair,currency='btc', amount=borrowing_amount,
#                          api_key=api,secret=sec,passphrase=passph,)
# TODO         FROM borrow_result check if ['result']==True and hold borrow_id in database or variable

#      SELL BORROWING AMOUNT
sell_result = margin_market_order(api_key=api,secret=sec,passphrase=passph, pair=pair, side='sell',
                                  amount=borrowing_amount)
# TODO check sell_result['result'] == true

