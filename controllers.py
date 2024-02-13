from flask import jsonify
from models import Books, session
from datetime import datetime
import utils

class Controllers:
   
    @staticmethod
    def get_all_books():
        """Retrieves all books from the database.

        Returns:
            list: A list of dictionaries representing the serialized books.
        """
        books = session.query(Books).all()
        return [book.serialize() for book in books]
       
    @staticmethod
    def get_book_by_id(id: int):
        """Retrieves a book by its ID from the database.

        Args:
            id (int): The ID of the book to retrieve.

        Returns:
            dict: A dictionary representing the serialized book.
        """
        book = session.query(Books).filter_by(id=id).first()
        
        if book:
            return book.serialize()
            
        else:
            return jsonify({"message": 'not found', "status": 404, "id": id, "date": datetime.utcnow()})
    
    @staticmethod
    def insert_new_book(json: dict):
        """Inserts a new book into the database.

        Args:
            json (dict): A dictionary containing the book details.

        Returns:
            dict: A dictionary containing a success message and status code.
        """
        validation = utils.validation_insert_json(json)
        
        if validation["status"] == 200:
            book = Books(
                book=validation.get("book"),
                author=validation.get("author"),
                synopsis=validation.get("synopsis"),
                content=validation.get("content"),
            )
            session.add(book)
            session.commit()
            return {"message": 'new book added successfully', "status": 200}
                    
        else:            
            return validation
                
    @staticmethod
    def delete_book(id):
        """Deletes a book from the database by its ID.

        Args:
            id (int): The ID of the book to delete.

        Returns:
            dict: A dictionary containing a success message and status code.
        """
        validation = utils.validation_id(id)
       
        if validation["status"] == 200:
            book = session.query(Books).filter_by(id=id).first()
           
            if book:
                session.delete(book)
                session.commit()
                return jsonify({"message": 'successfully deleted book', "id": id, "status": 200})
            else:
                return jsonify({"message": 'Book not found', "id": id, "status": 404})
        else:
            return jsonify({"message": 'Id not found', "id": id, "status": 404})
    
    @staticmethod
    def edit_book(json: dict):
        """Edits an existing book in the database.

        Args:
            json (dict): A dictionary containing the book details to edit.

        Returns:
            dict: A dictionary containing a success message and status code.
        """
        if utils.validation_id(json['id'])["status"] == 200:
            validation = utils.validation_edit_json(json)
            if validation:
                edited_columns = [x for x in validation.keys()] 
                book = session.query(Books).filter_by(id=json["id"]).first()
                if validation["book"]:
                    book.book = validation.get("book")
                if validation["author"]:
                    book.author = validation.get("author")
                if validation["synopsis"]:
                    book.synopsis = validation.get("synopsis")
                if validation["content"]:
                    book.content = validation.get("content")
                session.commit()
                return jsonify({"message": f'Edited columns {edited_columns}', "status": 200})
            else:
                return validation
        else:
            return jsonify({"message": 'id not informed', "status": 400})