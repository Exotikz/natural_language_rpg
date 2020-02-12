from pymongo import MongoClient

""" https://docs.mongodb.com/v2.6/reference/sql-comparison/ """
class MongoDBConnection(object):

    """MongoDB Connection"""    
    def __init__(self, host='localhost', port=27017):
        self.host = host
        self.port = port
        self.connection = None   

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self    
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def connect_to_db(self, db):
        return self.connection[db]

""" Query the specific collection.
"""
def query_collection(db, collection, key, value):
    with MongoDBConnection() as mongo:
        return mongo.connect_to_db(db)[collection].find( {key: value} )
