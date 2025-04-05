from flask import app, jsonify, request, abort

books = {
    1: {"title": "Book 1", "author": "Author 1"},
    2: {"title": "Book 2", "author": "Author 2"},
    3: {"title": "Book 3", "author": "Author 3"},
}


def get_all_books():
    return jsonify({"status": "success", "data": books})


def get_book(book_id):
    book = books.get(book_id)
    if not book:
        abort(404, description="Book not found")

    return jsonify({"status": "success", "data": book})


def add_book():
    data = request.get_json()

    if not data or not data.get("title") or not data.get("author"):
        abort(400, description="Missing title or author in request")

    new_book_id = len(books) + 1
    new_book = {
        "title": data["title"],
        "author": data["author"]
    }

    books[new_book_id] = new_book
    return jsonify({"status": "success", "message": "Book created!"}), 201


def delete_book(book_id):
    book = books.pop(book_id, None)
    if not book:
        abort(404, description="Book not found")

    return jsonify({"status": "success", "message": f"Book {book_id} deleted!"})


def update_book(book_id):
    book = books.get(book_id)
    if not book:
        abort(404, description="Book not found")

    data = request.get_json()
    if not data:
        abort(400, description="No data provided to update")

    # Update book fields
    for key, value in data.items():
        if key in book and value:
            book[key] = value

    return jsonify({"status": "success", "message": f"Book {book_id} modified!"}), 200
