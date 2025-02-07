# import flask
from flask import Flask, request, redirect, url_for, session, make_response, flash, render_template
from flask_cors import CORS, cross_origin
#from authlib.integrations.flask_client import OAuth


# from flask_session import Session

# set up flask app
app = Flask(__name__, static_url_path='')
app.secret_key = 'super_secret'
CORS(app, supports_credentials=False)
#CORS(app)
#oauth = OAuth(app)


# cors = CORS(app, resources={r"/foo": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'
# api = Api(app)

# @app.before_request
# def before_request():
#     request.headers.add('Cross-Origin-Opener-Policy', 'same-origin-allow-popups')
# @app.after_request
# def after_request(response):
#
#     response.headers.add('Cross-Origin-Opener-Policy', 'same-origin-allow-popups')
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#     return response


# redirect to our static home page
@app.route('/', methods=['GET'])
def home():
    return "hello world"
    return redirect('../home.html')


@app.route('/login', methods=['GET'])
#@cross_origin()
def login():
    return redirect('../user_login.html')


@app.route('/session/spellbook_id', methods=['GET'])
def session_spellbook_id():
    session['spellbook_id'] = 1
    return str(session.get('spellbook_id'))


@app.route('/session/user_id', methods=['GET'])
def session_user_id():
    session['user_id'] = 1
    return str(session.get('user_id'))
