Algo for opening orders:
  -Okex:
      -In okex we have 2 accounts. Spot and Margin account. We have everything in the spot account. Lets consider arbitraging Eth/Btc.
      We transfer from spot account x BTC in Margin account and we specify the pair. In our case the pair is eth/btc. The command should be 
      something like transfer(api_key,secret_key,passphrase, from_account=spot,to_account=margin,how_many=x,token=BTC,pair=ETH/BTC)
      -Then we get a loan of eth. The maximum loan we can get is 2*x/(eth/btc) where x is the transfered bitcoin ammount. Okex fee for this is 0.2%
      -Then you should find out how many eth you borrowed. In the loan function you can specify an id with wich you can later find out info
      about your loan. after you find out how many eth you borrowed you sell them for btc. You must know how many btc you bought.Lets say Y.
  -Hitbtc:
      You market_buy eth 
      
Algo for closing orders
  -okex:
    -You buy back eth with Y btc.
    -You repay your loan
    -you transfer your btc to your spot account
  -hitbtc
    -You sell the eth for btc
    
When taking a loan margin_buying btc and eth you must be very careful with the fees.
