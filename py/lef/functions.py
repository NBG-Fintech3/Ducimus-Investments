def okex_to_binance(pair):
    pair = pair[0:(pair.find('_'))] + pair[pair.find('_')+1 :]
    if ('usd' in pair):
        pair +='t'
    return pair.upper()


def okex_to_hitbtc(pair):
    pair = pair[0:(pair.find('_'))] + pair[pair.find('_')+1 :]
    if 'usdt' in pair:
        pair = pair[:-1]
    return pair.upper()


def hitbtc_to_okex(pair):
    pair = pair.lower()
    if 'usd' in pair:
        pair = pair[:-3] + '_' + pair[-3:] + 't'
    else:
        pair = pair[:-3] + '_' + pair[-3:]
    return pair


def arb(okexPrice,hitbtcPrice):
    #if hitbtcPrice > okexPrice: return 0
    arbi = ((okexPrice-hitbtcPrice)/hitbtcPrice )
    arbi *=100
    #if arbi < 0 : return 0
    return arbi


def no_spaces(string):
    string = str(string)
    ret = ''
    for i in range(len(string)):
        if string[i] != ' ':
            ret += string[i]
    return ret


def orderJson(jsonList):
    lines = sorted(jsonList, key=lambda k: k['arbitrage'], reverse=True)
    return lines


