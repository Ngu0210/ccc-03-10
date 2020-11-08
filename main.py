from flask import Flask, request, jsonify
app = Flask(__name__)
from controller import registerable_controllers

for controller in registerable_controllers:
    app.register_blueprint(controller)
