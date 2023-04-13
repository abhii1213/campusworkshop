"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq4v02qv2dcb92rdmg-a",
        database="todo_95p6",
        user="root",
        password="6m6om4iwskcc1MNNa9rWPkog81B5C3og")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
