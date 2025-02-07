# import our get connection function
from utils import dbconfig


# pull a specific user from the database
def get_user(user_id):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "SELECT * FROM users WHERE user_id = ?"
        # execute our query
        cursor.execute(query, user_id)
        # fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result