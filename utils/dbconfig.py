# import connect function in order to establish a connection to out database using pyodbc
from pyodbc import connect

import pymongo

# import os to pull our environment variables
import os

# get db credentials from system variables so that they aren't exposed in code
#db_url = os.environ['db_url']
#db_username = os.environ['db_username']
#db_password = os.environ['db_password']
#db_name = ''


# this function will return a new connection to the database
def get_connection():
    # return connect("jdbc:postgresql://spellbook-1.clklzl8qupep.us-east-2.rds.amazonaws.com:5432/postgres")
    #return connect("DRIVER=PostgreSQL UNICODE(x64);SERVER=spellbook-1.clklzl8qupep.us-east-2.rds.amazonaws.com;"
    #               "PORT=5432;DATABASE=postgres;UID=postgres;PWD=password; sslrootcert=us-east-2-bundle; sslmode=verify-full")
    return connect("DRIVER=PostgreSQL UNICODE(x64);SERVER=localhost;PORT=5432;DATABASE=postgres;UID=postgres;PWD=password;Trusted_Connection=no;BoolsAsChar=0")
    return connect(f"DRIVER={{PostgreSQL UNICODE(x64)}};SERVER={db_url};PORT=5432;DATABASE={db_name};UID={db_username};PWD={db_password};Trusted_Connection=no;BoolsAsChar=0")


def get_mongo_connection():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    return client
