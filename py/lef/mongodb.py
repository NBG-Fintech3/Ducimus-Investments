from pymongo import MongoClient

class mongodb():
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['arbitrage']
        self.col =self.db['arbitrage']

    def insertone(self,json):
        self.col.insert_one(json)

try1 = mongodb()
try1.insertone({'a':'a'})