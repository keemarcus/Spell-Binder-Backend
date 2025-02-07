# import our flask app and database connection/cursor from app.py
import datetime

from src.app import app, request, session, redirect

# import our service level logic for reimbursements
import src.service.deck_service as deck

# import json formatting logic
from src.models.deck import DeckEncoder
from json import dumps

# set up logging
import logging


@app.route('/user/<int:user_id>/deck/<string:deck_name>', methods=['GET'])
def get_deck(user_id, deck_name):
    result = deck.get_deck(user_id, deck_name)
    result = dumps(result, cls=DeckEncoder)

    # return the result in json form
    return result, 200


@app.route('/insert', methods=['POST'])
def insert_deck():
    data = request.get_json()
    result = deck.insert_deck(data)

    # return the result
    return result, 200


@app.route('/replace/<string:deck_id>', methods=['PUT'])
def replace_deck(deck_id):
    data = request.get_json()
    result = deck.replace_deck(deck_id, data)

    # return the result
    return result, 200

