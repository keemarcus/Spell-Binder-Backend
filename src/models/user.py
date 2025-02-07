# import JSONEncoder to set up our custom encoder
from json import JSONEncoder


class User:
    # constructor
    def __init__(self, _user_id, _username):
        self.user_id = _user_id
        self.username = _username

    # getters
    def get_id(self):
        return self.user_id

    def get_username(self):
        return self.username

    # setters
    def set_id(self, user_id):
        self.user_id = user_id

    def set_username(self, username):
        self.username = username


# custom encoder
class UserEncoder(JSONEncoder):
    # override the default method
    def default(self, user):
        if isinstance(user, User):
            return user.__dict__
        else:
            return JSONEncoder.default(self, user)
