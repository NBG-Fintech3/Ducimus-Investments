from pymongo import MongoClient
import pymysql


class mongodb():
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['arbitrage']
        self.col =self.db['arbitrage']

    def insertone(self,json):
        self.col.insert_one(json)


class mysqldb():
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          port = 3306,
                                          user = 'root',
                                          db = 'trading_db',
                                          password='',
                                          charset='utf8mb4',
                                          cursorclass= pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()

    def post_arbitrage_pairs(self, pairs_list):
        #list of jsons {'pair': ...., 'arbitrage':... }
        sql = 'INSERT INTO `arbitrage`(`pair`,`arbitrage`) VALUES (%s,%s)'
        for data in pairs_list:

            result = self.cursor.execute(sql,(data['pair'],data['arbitrage']))

        return 1

trial = mysqldb()
pairs_list = [{'pair':'btc_usd', 'arbitrage':'1.5045'}]
trial.post_arbitrage_pairs(pairs_list)