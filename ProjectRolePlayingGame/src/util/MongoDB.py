from pymongo import MongoClient

# https://docs.mongodb.com/v2.6/reference/sql-comparison/
class MongoDBConnection(object):
    """MongoDB Connection"""    
    # mongod.exe --dbpath="ProjectRolePlayingGame/resources/db"
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

def query_specific_element(db, collection, key, value):
    """ Query the specific collection.
    """
    with MongoDBConnection() as mongo:
        return mongo.connect_to_db(db)[collection].find( {key: value} )

def query_collection(db, collection):
    """ Query the specific collection.
    """
    with MongoDBConnection() as mongo:
        return mongo.connect_to_db(db)[collection].find()

def insert_to_collection(db, collection, element):
    """ Stocking the object.
    """
    with MongoDBConnection() as mongo:
        return mongo.connect_to_db(db)[collection].insert_one( element )

def update_to_collection(db, collection, where, element):
    """ Updating the object
    """
    with MongoDBConnection() as mongo:
        return mongo.connect_to_db(db)[collection].update( where, element )