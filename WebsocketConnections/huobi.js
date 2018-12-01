var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

const WS_URL = 'wss://api.huobi.pro/ws';
var dbo;

var orderbook = {};

MongoClient.connect(url, {useNewUrlParser : true}, async function(err, db) {
    if (err) throw err;
    dbo = db.db("huobi");


    dbo.createCollection("btcusdt", function(err, res) {
        if (err) throw err;
            console.log("Collection created!");
    }) 
})  


function handle(data) {
    // console.log('received', data.ch, 'data.ts', data.ts, 'crawler.ts', moment().format('x'));
    let symbol = data.ch.split('.')[1];
    let channel = data.ch.split('.')[2];
    switch (channel) {
        case 'depth':
            console.log("Depth update on :" + symbol);
            console.log(data.tick);
            orderbook[symbol] = data.tick;
            break;
        case 'kline':
            console.log('kline', data.tick);
            break;
    }

    let json = new Object; 
    json['symbol'] = symbol;
    json['timestamp'] = Date.now(); 
    json['orderbook'] = data.tick; 
    dbo.collection(symbol).insertOne(json);


}

function subscribe(ws) {

    var symbols = new Array;

//GET PAIRS WITH DAILY VOLUME ABOVE 100,000 

axios.get('https://api.huobi.pro/market/tickers')
  .then(response => {
    data = response.data.data; 
    console.log(data);

   for ( let  obj of data){ 
        let symbol = obj.symbol; 
        if(symbol == 'ethusdt')
            var ethprice = obj.buy;
        
        if(symbol == 'btcusdt')
            var btcprice = obj.buy;

        if(symbol == 'htusdt')   //huobi token 
            var htprice = obj.buy; 
   }


    for ( let obj of data){

        let symbol = obj.symbol; 
        console.log(obj.symbol); 
            
        let base = symbol.slice(-3);

        if(base == 'eth')
            obj.vol = obj.vol * ethprice;

        else if (base == 'btc')
            obj.vol = obj.vol * btcprice;

        
        base = base.slice(-2);
        if( base == 'ht')

            obj.vol = obj.vol *htprice;

        if(obj.vol > 100000) 
            symbol = "'" + symbol + "'"; 
    
   
            symbols.push(symbol);

    }


    for (let symbol of symbols) {
        ws.send(JSON.stringify({
            "sub": `market.${symbol}.depth.step0`,
            "id": `${symbol}`
        }));
    }


    // 订阅K线
//     for (let symbol of symbols) {
//         ws.send(JSON.stringify({
//             "sub": `market.${symbol}.kline.1min`,
//             "id": `${symbol}`
//         }));
//     }
})
}



function init() {

    var ws = new WebSocket(WS_URL);
    
    ws.on('open', () => {
        console.log('open');
        subscribe(ws);
    });
    
    ws.on('message', (data) => {
        let text = pako.inflate(data, {
            to: 'string'
        });
        
        let msg = JSON.parse(text);
        if (msg.ping) {
            ws.send(JSON.stringify({
                pong: msg.ping
            }));
        } else if (msg.tick) {
            // console.log(msg);
            handle(msg);
        } else {
            console.log(text);
        }


      
    })


    ws.on('close', () => {
        console.log('close');
        init();
    });
    ws.on('error', err => {
        console.log('error', err);
        init();
    });

} 


init();
