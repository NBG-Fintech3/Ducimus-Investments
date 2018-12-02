# Ducimus-Investments
Automated crypto trading exploiting arbitrage opportunities and market making.

The trading platform is at beta stage, version 0.1 commited 2nd of December, 2018 17:10.
It is based on PHP5.6 technology using via shell terminal python scripted algorithms that trace arbitrage opportunities between OKEX & HITBTC crypto exchanges.

Two types of store databases are used:
1) MySQL MariaDB using phpmyadmin as database administration tool.
2) MongoDB in order to collect orderbook data and make statistical analysis for tracing arbitrage.

The arbitrage is traced manually via REST-API technology between server & client and in a future version sockets will be used or an upgrade to Google Firebase realtime database.

The platform is deployed on Google Cloud platform.
