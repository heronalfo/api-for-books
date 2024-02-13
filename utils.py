from models import session, Books

def validation_insert_json(json: dict):
    """Validates JSON data for inserting a new book into the database.

    Args:
        json (dict): A dictionary containing book details.

    Returns:
        dict: A dictionary containing a success message and status code if valid,
              otherwise, a dictionary containing an error message and status code.
    """
    if not json:
        return {"message": 'No arguments were passed, database sent is invalid', "status": 400}
    
    if not all(json.get(param) for param in ["book", "author", "synopsis", "content"]):
        return {"message": 'Missing or null values for required parameters', "status": 400}
  
    if (book_length:= len(json.get("book"))) > 100:
        return {"message": f'the parameter "book" must contain less 100 characters, however, they were passed {book_length} characters'}
    
    if (author_length:= len(json.get("author"))) > 200:
        return {"message": f'the parameter "author" must contain less 100 characters, however, they were passed {author_length} characters'}
           
    json["status"] = 200       
    return json

def validation_edit_json(json: dict):
    """Validates JSON data for editing an existing book in the database.

    Args:
        json (dict): A dictionary containing book details.

    Returns:
        dict: A dictionary containing valid book data to update in the database.
    """
    data = {}
        
    if not json:
        return {"message": 'No arguments were passed, database sent is invalid', "status": 400}
    
    if book:= json.get("book"): 
        if (book_length:= len(book)) > 100:
            return {"message": f'the parameter "book" must contain less 100 characters, however, they were passed {book_length} characters'}
        data["book"] = book
    
    if author:= json.get("author"):
        if (author_length:= len(author)) > 200:
            return {"message": f'the parameter "author" must contain less 100 characters, however, they were passed {author_length} characters'}
        data["author"] = author
    
    if synopsis:= json.get("synopsis"):               
        data["synopsis"] = synopsis
    
    if content:= json.get("content"):               
        data["content"] = content
                
    return data
    
def validation_id(id: int):
    """Validates book ID.

    Args:
        id (int): The ID of the book.

    Returns:
        dict: A dictionary containing a success message and status code if valid,
              otherwise, a dictionary containing an error message and status code.
    """
    book = session.query(Books).filter_by(id=id).first()
    
    if book is None:
        return {"message": 'Id not found', 'status': 404}
    else:
        return {"message": 'successfully', "status": 200}