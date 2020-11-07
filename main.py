from flask import Flask, request, jsonify
app = Flask(__name__)
from books import books
app.register_blueprint(books)
