import src.dao.user_dao as dao
from src.models.user import User
from utils import dbconfig


def get_user(index):
    db_user = dao.get_user(index)
    return User(db_user[0], db_user[1])
