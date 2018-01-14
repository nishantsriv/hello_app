import datetime
import flask
from flask import Flask

app = Flask(__name__)
app.secret_key = 'something web customer secret'

from src.controllers import hello_controller
