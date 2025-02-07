# import our flask app and database connection/cursor from app.py
import datetime

from src.app import app, request, session, redirect

# import our service level logic for reimbursements
import src.service.user_service as user

# import json formatting logic
from src.models.user import UserEncoder
from json import dumps

# set up logging
import logging


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # use service layer logic to get results
    result = user.get_user(user_id)
    result = dumps(result, cls=UserEncoder)

    # return the result in json form
    return result, 200
