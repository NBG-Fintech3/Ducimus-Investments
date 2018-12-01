// On open get volume of pairs > 100000 and subscribe to channels
ws.on('open', function open () {


axios.get('https://www.okex.com/api/v1/tickers.do')
  .then(response => {
    tickers = response.data.tickers; 
    //console.log(tickers);

   for ( let  obj of tickers){ 
      let symbol = obj.symbol; 
      if(symbol == 'eth_usdt')
        var ethprice = obj.buy;
      
      if(symbol == 'btc_usdt')
        var btcprice = obj.buy;

      if(symbol == 'okb_usdt')
        var okbprice = obj.buy; 
   }


    for ( let obj of tickers){

      let symbol = obj.symbol; 
      //console.log(obj.symbol); 
        
      let base = symbol.slice(-3);

      if(base == 'eth')
        obj.vol = obj.vol * ethprice;

      else if (base == 'btc')
        obj.vol = obj.vol * btcprice;

      else if( base == 'okb')
        obj.vol = obj.vol *okbprice;

      if(obj.vol > 100000) {
        //symbol = "'{" + '"channel":"ok_sub_spot_' + symbol + '_depth","event":"addChannel"}' + "'"; 
        symbol = '{"channel":"ok_sub_spot_' + symbol + '_depth","event":"addChannel"}'; 
        ws.send(symbol);

        
        console.log("Connected to : " + symbol);
      }
    }
  })
})



 MongoClient.connect(url, {useNewUrlParser : true}, function(err, db) {
  if (err) throw err;
  var dbo = db.db("okex");
  

  dbo.createCollection("ltc_btc", function(err, res) {
    if (err) throw err;
    console.log("Collection created!");
 }

);


  ws.on('message', function incoming (data) {
    
    
    if (data instanceof String) {
      console.log(data);
    } else {
     
      try {
        //console.log(pako.inflate(data));
        dataNew = pako.inflateRaw(data, {to: 'string'}); 
        dataNew = dataNew.slice(1, dataNew.length - 1 );
        dataNew = JSON.parse(dataNew);
        data = dataNew; 
        symbol = (data.channel).slice(12, (data.channel).length - 6);
        console.log(symbol);
        
        if(data.binary == 0)
          dbo.collection(symbol).insertOne(data);
      } catch (err) {
        console.log(err); 
      }
    }

   
  })



});

