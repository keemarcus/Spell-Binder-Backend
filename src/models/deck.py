# import JSONEncoder to set up our custom encoder
from json import JSONEncoder


class Deck:
    # constructor
    def __init__(self, _deck_id, _user_id, _deck_name, _deck_json):
        self.deck_id = _deck_id
        self.user_id = _user_id
        self.deck_name = _deck_name
        self.deck_json = _deck_json

    # getters
    def get_deck_id(self):
        return self.deck_id

    def get_user_id(self):
        return self.user_id

    def get_deck_name(self):
        return self.deck_name

    def get_deck_json(self):
        return self.deck_json

    # setters
    def set_deck_id(self, deck_id):
        self.deck_id = deck_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_username(self, deck_name):
        self.deck_name = deck_name

    def set_deck_json(self, deck_json):
        self.deck_name = deck_json


# custom encoder
class DeckEncoder(JSONEncoder):
    # override the default method
    def default(self, deck):
        if isinstance(deck, Deck):
            return deck.__dict__
        else:
            return JSONEncoder.default(self, deck)
