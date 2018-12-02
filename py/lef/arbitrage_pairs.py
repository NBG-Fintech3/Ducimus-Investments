import buttons_actions as act

result = act.arbitrageJsonList()

for j in result:
    print('Pair: ',j['pair'],' with arbitrage:',j['arbitrage'])

