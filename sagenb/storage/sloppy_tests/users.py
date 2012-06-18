from sage.all import *

from sagenb.notebook.user import User
from sagenb.notebook.user_manager import SimpleUserManager
U = SimpleUserManager()

users = {'admin': User('admin','abc','a@b.c','admin'), 'wstein': User('wstein','xyz','b@c.d','user')}

from sagenb.storage import MongoDBDatastore

from pymongo import Connection

c = Connection()
db = c.test_database

ds = MongoDBDatastore(db, tmp_dir())
ds.save_users(users)
users = ds.load_users(U)

print U.users()