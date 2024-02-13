---

## API Documentation

### Introduction
This documentation describes the API for book management. The API allows retrieving, inserting, editing, and deleting information about books.

### Base URL
`/api/books/`

### Routes
1. **GET /api/books/**  
   Retrieves all books.
   
2. **GET /api/books/<int:id>/**  
   Retrieves a specific book by its ID.
   
3. **POST /api/books/insert_new_book/**  
   Inserts a new book.
   
4. **DELETE /api/books/delete_book/<int:id>/**  
   Deletes a book by its ID.
   
5. **PATCH /api/books/edit_book/**  
   Edits an existing book.

### Request Parameters
- **id (int)**: The ID of the book.
- **book (str)**: The title of the book.
- **author (str)**: The author of the book.
- **synopsis (str)**: The synopsis of the book.
- **content (str)**: The content of the book.

### Usage Examples
1. **Retrieve all books**  
   **Method**: GET  
   **URL**: `/api/books/`  
   **Example Response**:  
   ```
   [
       {
           "id": 1,
           "book": "Book A",
           "author": "Author A",
           "synopsis": "Synopsis of Book A",
           "content": "Content of Book A"
       },
       {
           "id": 2,
           "book": "Book B",
           "author": "Author B",
           "synopsis": "Synopsis of Book B",
           "content": "Content of Book B"
       }
   ]
   ```

2. **Retrieve a specific book**  
   **Method**: GET  
   **URL**: `/api/books/1/`  
   **Example Response**:  
   ```
   {
       "id": 1,
       "book": "Book A",
       "author": "Author A",
       "synopsis": "Synopsis of Book A",
       "content": "Content of Book A"
   }
   ```

3. **Insert a new book**  
   **Method**: POST  
   **URL**: `/api/books/insert_new_book/`  
   **Request Body**:  
   ```
   {
       "book": "New Book",
       "author": "New Author",
       "synopsis": "New Synopsis",
       "content": "New Content"
   }
   ```

4. **Delete a book**  
   **Method**: DELETE  
   **URL**: `/api/books/delete_book/1/`  
   **Example Response**:  
   ```
   {
       "message": "successfully deleted book",
       "status": 200
   }
   ```

5. **Edit an existing book**  
   **Method**: PATCH  
   **URL**: `/api/books/edit_book/`  
   **Request Body**:  
   ```
   {
       "id": 1,
       "book": "Edited Book",
       "author": "Edited Author",
       "synopsis": "Edited Synopsis",
       "content": "Edited Content"
   }
   ```

### Example Responses
- **200 OK**: The request was successful.
- **400 Bad Request**: The request is invalid or missing parameters.
- **404 Not Found**: The requested resource was not found.
- **405 Method Not Allowed**: The request method is not allowed for the requested resource.

---