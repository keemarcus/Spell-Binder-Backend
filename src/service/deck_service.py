import src.dao.deck_dao as dao
from src.models.deck import Deck
from json import dumps
from src.models.deck import DeckEncoder


def get_deck(user_id, deck_name):
    db_deck = dao.get_deck(user_id, deck_name)
    return Deck(str(db_deck['_id']), db_deck['user_id'], db_deck['deck_name'], db_deck['cards'])


def insert_deck(new_deck_json):
    # make sure the new deck json is valid
    new_deck = Deck(None, new_deck_json['user_id'], new_deck_json['deck_name'], new_deck_json['deck_json'])
    return dao.insert_deck(new_deck_json)


def replace_deck(deck_id, new_deck_json):
    # make sure the new deck json is valid
    new_deck = Deck(None, new_deck_json['user_id'], new_deck_json['deck_name'], new_deck_json['deck_json'])
    return dao.replace_deck(deck_id, new_deck_json)



