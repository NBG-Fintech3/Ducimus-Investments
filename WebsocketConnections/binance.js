// Original Code from : https://github.com/jaggedsoft/node-binance-api

const fs = require('fs');

const binance = require('node-binance-api')().options({
  APIKEY: '<key>',
  APISECRET: '<secret>',
  useServerTime: true, // If you get timestamp errors, synchronize to server time at startup
  test: true // If you want to use sandbox mode where orders are simulated
});

var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";
var pairs = new Array;


function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}




sleep(2000).then( () => { 
/* Connecting to Database function and depthcache updates */

 MongoClient.connect(url, {useNewUrlParser : true}, async function(err, db) {
  if (err) throw err;
  var dbo = db.db("Binance");
  

  dbo.createCollection("BTC_USDT", function(err, res) {
    if (err) throw err;
    console.log("Collection created!");
 }

);



binance.websockets.depthCache(['ETHBTC','LTCBTC','BNBBTC','NEOBTC','QTUMETH','EOSETH','SNTETH','BNTETH','BCCBTC','GASBTC','BNBETH','ETHUSDT','HSRBTC','OAXETH','DNTETH','MCOETH','ICNETH','MCOBTC','WTCBTC','WTCETH','LRCBTC','LRCETH','QTUMBTC','YOYOBTC','OMGBTC','OMGETH','ZRXBTC','ZRXETH','STRATBTC','STRATETH','SNGLSBTC','SNGLSETH','BQXBTC','BQXETH','KNCBTC','KNCETH','FUNBTC','FUNETH','SNMBTC','SNMETH','NEOETH','IOTABTC','IOTAETH','LINKBTC','LINKETH','XVGBTC','XVGETH','SALTBTC','SALTETH','MDABTC','MDAETH','MTLBTC','MTLETH','SUBBTC','SUBETH','EOSBTC','SNTBTC','ETCETH','ETCBTC','MTHBTC','MTHETH','ENGBTC','ENGETH','DNTBTC','ZECBTC','ZECETH','BNTBTC','ASTBTC','ASTETH','DASHBTC','OAXBTC','ICNBTC','BTGBTC','BTGETH','EVXBTC','EVXETH','REQBTC','REQETH','VIBBTC','VIBETH','TRXBTC','TRXETH','POWRBTC','POWRETH','ARKBTC','ARKETH','YOYOETH','XRPBTC','XRPETH','MODBTC','MODETH','ENJBTC','ENJETH','STORJBTC','STORJETH','BNBUSDT','VENBNB','YOYOBNB','POWRBNB','VENBTC','VENETH','KMDBTC','KMDETH','RCNBTC','RCNETH','RCNBNB','NULSBTC','NULSETH','RDNBTC','RDNETH','RDNBNB','XMRBTC','XMRETH','DLTBNB','DLTBTC','DLTETH','AMBBTC','AMBETH','AMBBNB','BCCETH','BATBTC','BATETH','BATBNB','BCPTBTC','BCPTETH','BCPTBNB','ARNBTC','ARNETH','GVTBTC','GVTETH','CDTBTC','CDTETH','GXSBTC','GXSETH','NEOUSDT','POEBTC','POEETH','QSPBTC','QSPETH','QSPBNB','BTSBTC','BTSETH','BTSBNB','XZCBTC','XZCETH','LSKBTC','LSKETH','TNTBTC','TNTETH','FUELBTC','FUELETH','MANABTC','MANAETH','BCDBTC','BCDETH','DGDBTC','DGDETH','IOTABNB','ADXBTC','ADXETH','ADXBNB','ADABTC','ADAETH','PPTBTC','PPTETH','CMTBTC','CMTETH','CMTBNB','XLMBTC','XLMETH','XLMBNB','CNDBTC','CNDETH','CNDBNB','LENDBTC','LENDETH','WABIBTC','WABIETH','WABIBNB','LTCETH','TNBBTC','TNBETH','WAVESBTC','WAVESETH','GTOBTC','GTOETH','GTOBNB','ICXBTC','ICXETH','ICXBNB','OSTBTC','OSTETH','OSTBNB','ELFBTC','ELFETH','AIONBTC','AIONETH','AIONBNB','NEBLBTC','NEBLETH','BRDBTC','BRDETH','BRDBNB','EDOBTC','EDOETH','WINGSBTC','WINGSETH','NAVBTC','NAVETH','LUNBTC','LUNETH','TRIGBTC','TRIGETH','TRIGBNB','APPCBTC','APPCETH','APPCBNB','VIBEBTC','VIBEETH','RLCBTC','RLCETH','INSBTC','INSETH','PIVXBTC','PIVXETH','IOSTBTC','IOSTETH','CHATBTC','CHATETH','STEEMBTC','STEEMETH','NANOBTC']//,'NANOETH','NANOBNB','VIABTC','VIAETH','VIABNB','BLZBTC','BLZETH','BLZBNB','AEBTC','AEETH','RPXBTC','RPXETH','RPXBNB','NCASHBTC','NCASHETH','NCASHBNB','POABTC','POAETH','POABNB','ZILBTC','ZILETH','ZILBNB','ONTBTC','ONTETH','ONTBNB','STORMBTC','STORMETH','STORMBNB','QTUMUSDT','XEMBTC','XEMETH','XEMBNB','WANBTC','WANETH','WANBNB','WPRBTC','WPRETH','QLCBTC','QLCETH','SYSBTC','SYSETH','SYSBNB','QLCBNB','GRSBTC','GRSETH','ADAUSDT','ADABNB','CLOAKBTC','CLOAKETH','GNTBTC','GNTETH','LOOMBTC','LOOMETH','LOOMBNB','XRPUSDT','BCNBTC','BCNBNB','REPBTC','REPETH','TUSDBTC','TUSDETH','TUSDBNB','ZENBTC','ZENETH','SKYBTC','SKYETH','EOSUSDT','EOSBNB','CVCBTC','CVCETH','CVCBNB','THETABTC','THETAETH','THETABNB','XRPBNB','TUSDUSDT','IOTAUSDT','XLMUSDT','IOTXBTC','IOTXETH','QKCBTC','QKCETH','AGIBTC','AGIETH','AGIBNB','NXSBTC','NXSETH','ENJBNB','DATABTC','DATAETH','ONTUSDT','TRXBNB','TRXUSDT','ETCUSDT','ICXUSDT','SCBTC','SCETH','SCBNB','NPXSBTC','NPXSETH','KEYBTC','KEYETH','NASBTC','NASETH','MFTBTC','MFTETH','MFTBNB','DENTBTC','DENTETH','ARDRBTC','ARDRETH','ARDRBNB','HOTBTC','HOTETH','VETBTC','VETETH','VETUSDT','VETBNB','DOCKBTC','DOCKETH','POLYBTC','POLYBNB','PHXBTC','PHXETH','PHXBNB','HCBTC','HCETH','GOBTC','GOBNB','PAXBTC','PAXBNB','PAXUSDT','PAXETH','RVNBTC','RVNBNB','DCRBTC']
, (symbol, depth) => {

	  
	  let bids = binance.sortBids(depth.bids);
	  let asks = binance.sortAsks(depth.asks);

	  console.log(symbol + " depth cache update");

	  //console.log('Asks : ', asks);
	  // console.log('Bids: ', bids);   

	  let asksArray = Object.entries(asks);
	  let bidsArray = Object.entries(bids);
	   
	 
	  
	  askslength = Object.keys(asks).length;
	  bidslength = Object.keys(bids).length; 

	  let i = 0;
	  let askjson = []; 
	 

	  while(i < askslength){
	   		let price = asksArray[i][0];
	   		let amount = asksArray[i][1]; 
	 		
	 		var temp = new Object;

	   		temp['id'] = i; 
	   		temp['amount'] = amount;
	   		temp['price'] = price; 
			//console.log("Price : " + price + "  Amount : " + amount);
	   		askjson.push(temp); 

	   		i++;
	  }

	  i = 0; 
	  let bidjson = []; 

	  while(i < bidslength){
	   		let price = bidsArray[i][0];
	   		let amount = bidsArray[i][1]; 
	 		
	 		var temp = new Object;

	   		temp['id'] = i; 
	   		temp['amount'] = amount;
	   		temp['price'] = price; 
			//console.log("Price : " + price + "  Amount : " + amount);
	   		bidjson.push(temp); 

	   		i++;
	  }

	  let json = new Object; 
	  json['symbol'] = symbol;
	  json['timestamp'] = Date.now(); 
	  json['asks'] = askjson;
	  json['bids'] = bidjson; 
	  dbo.collection(symbol).insertOne(json); 



