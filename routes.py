from flask import Blueprint, jsonify, request
import controllers

books = Blueprint('actions', __name__)
controllers = controllers.Controllers()

@books.route('/', methods=['GET'])
def get_all_books():
    """Retrieves all books from the database.

    Returns:
        dict: A dictionary containing serialized book data.
    """
    if request.method == 'GET':
        books = controllers.get_all_books()
        return jsonify(books)
    else:
        return jsonify({"message": 'method not allowed', "status": 405})

@books.route('<int:id>/', methods=['GET'])
def get_book_by_id(id):
    """Retrieves a book by its ID from the database.

    Args:
        id (int): The ID of the book to retrieve.

    Returns:
        dict: A dictionary containing serialized book data.
    """
    if request.method == 'GET':
        book = controllers.get_book_by_id(id=id)
        return jsonify(book)
    else:
        return jsonify({"message": 'method not allowed', "status": 405})

@books.route('insert_new_book/', methods=['POST'])
def insert_new_book():
    """Inserts a new book into the database.

    Returns:
        dict: A dictionary containing a success message and status code.
    """
    if request.method == 'POST':
        json = request.json
        book = controllers.insert_new_book(json)
        return jsonify(book)
    else:
        return jsonify({"message": 'method not allowed', "status": 405})

@books.route('delete_book/<int:id>/', methods=["DELETE"])
def delete_book(id):
    """Deletes a book from the database by its ID.

    Args:
        id (int): The ID of the book to delete.

    Returns:
        dict: A dictionary containing a success message and status code.
    """
    if request.method == 'DELETE':
        book = controllers.delete_book(id)
        return jsonify(book)
    else:
        return jsonify({"message": 'method not allowed', "status": 405})

@books.route('edit_book/', methods=["PATCH"])
def edit_book():
    """Edits an existing book in the database.

    Returns:
        dict: A dictionary containing a success message and status code.
    """
    if request.method == "PATCH":
        json = request.json
        validation = controllers.edit_book(json)
        return validation
    else:
        return jsonify({"message": 'method not allowed', "status": 405})