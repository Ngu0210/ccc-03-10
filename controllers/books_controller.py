from models.Book import Book
from main import db
from schemas.BookSchema import book_schema, books_schema
from flask import Blueprint, request, jsonify
books = Blueprint('books', __name__, url_prefix="/books")

@books.route("/", methods=["GET"])
def book_index():
    books = Book.query.all()
    return jsonify(books_schema.dump(books))

# @books.route("/", methods=["POST"])
# def book_create():
#     #Create a new book
#     sql = "INSERT INTO books (title) VALUES (%s);"
#     cursor.execute(sql, (request.json["title"],))
#     connection.commit()

#     sql = "SELECT * FROM books ORDER BY ID DESC LIMIT 1"
#     cursor.execute(sql)
#     book = cursor.fetchone()
#     return jsonify(book)

@books.route("/", methods=["POST"])
def book_create():
    #Create a new book
    book_fields = book_schema.load(request.json)

    new_book = Book()
    new_book.title = book_fields["title"]
    
    db.session.addx(new_book)
    db.session.commit()
    
    return jsonify(book_schema.dump(new_book))

# @books.route("/<int:id>", methods=["GET"])
# def book_show(id):
#     #Return a single book
#     sql = "SELECT * FROM books WHERE id = %s;"
#     cursor.execute(sql, (id,))
#     book = cursor.fetchone()
#     return jsonify(book)

# @books.route("/<int:id>", methods=["PUT", "PATCH"])
# def book_update(id):
#     #Update a book
#     sql = "UPDATE books SET title = %s WHERE id = %s;"
#     cursor.execute(sql, (request.json["title"], id))
#     connection.commit()

#     sql = "SELECT * FROM books WHERE id = %s"
#     cursor.execute(sql, (id,))
#     book = cursor.fetchone()
#     return jsonify(book)

# @books.route("/<int:id>", methods=["DELETE"])
# def book_delete(id):
#     sql = "SELECT * FROM books WHERE id = %s;"
#     cursor.execute(sql, (id,))
#     book = cursor.fetchone()
    
#     if book:
#         sql = "DELETE FROM books WHERE id = %s;"
#         cursor.execute(sql, (id,))
#         connection.commit()

#     return jsonify(book)