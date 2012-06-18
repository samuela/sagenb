from sage.all import *

from sagenb.storage import MongoDBDatastore

from pymongo import Connection

c = Connection()
db = c.test_database

ds = MongoDBDatastore(db, tmp_dir())

ds.save_user_history("joe_bob", ["a", "b", "c"])
print ds.load_user_history("joe_bob")