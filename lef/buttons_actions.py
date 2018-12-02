from functions import *
import databases
import time
import okex
import hitbtc


mongo = databases.mongodb()
sql = databases.mysqldb()


def same_pairs():
    okex_tickers = okex.okex_all_symbols()
    hitbtc_tickers = hitbtc.hitbtc_all_symbols()
    list = []
    for i in range(len(okex_tickers)):
        okex_pair = okex_tickers[i]['symbol']
        okex_pair = okex_to_hitbtc(okex_pair)
        for j in range(len(hitbtc_tickers)):
            hitbtc_pair = hitbtc_tickers[j]['symbol']

            if (okex_pair) == hitbtc_pair:

                list.append(hitbtc_pair)
    return list


def arbitrageJsonList():
    okex.okex_all_symbols()
    okex_tickers = okex.get_margin_tickers()
    hitbtc_tickers = hitbtc.hitbtc_all_symbols()

    arb_list = []
    same = same_pairs()
    for i in range(len(okex_tickers)):
        okex_pair = okex_tickers[i]['symbol']
        okex_pair = okex_to_hitbtc(okex_pair)
        if okex_pair in same:
            for j in range(len(hitbtc_tickers)):
                hitbtc_pair = hitbtc_tickers[j]['symbol']
                if hitbtc_pair in same:
                    if okex_pair == hitbtc_pair:
                        okex_bid = float(okex_tickers[i]['sell'])
                        binance_ask = float(hitbtc_tickers[j]['ask'])

                        arbi = arb(okex_bid, binance_ask)

                        #if arbi>0:
                        a = {
                            'pair':hitbtc_pair,
                            'arbitrage':arbi
                        }
                        arb_list.append(a)
    length = len(arb_list)
    for _ in range(length+1,10):
        arb_list.append({
            'pair': '',
            'arbitrage':0,

        })
    if length>10:
        arb_list = arb_list[:10]

    arb_list = orderJson(arb_list)

    return(arb_list)