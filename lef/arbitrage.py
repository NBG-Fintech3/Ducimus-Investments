import buttons_actions
from okex import okex_pair_data
from hitbtc import hitbtc_pair_data


btc_okex = okex_pair_data('btc_usdt')
btc_hitbtc = hitbtc_pair_data('BTCUSD')

okprice = float(btc_okex['last'])
hitprice = float(btc_hitbtc['last'])

print(100* (okprice-hitprice)/hitprice)