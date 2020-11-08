import psycopg2
from flask_sqlalchemy import SQLAlchemy

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://app:Testing1@localhost:5432/library_api"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return db  

connection = psycopg2.connect(
    database="library_api",
    user="app",
    password="Testing1",
    host="localhost"
)

cursor = connection.cursor()

print("connection open")

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")

print("connection executed")

connection.commit()

print("connection ended")
