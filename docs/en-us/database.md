---

## Database Documentation

### Table Structure

The `Books` table has the following fields:

- **id (Integer, primary key)**: The unique identifier of the book.
- **book (String, 100 characters, not null)**: The title of the book.
- **author (String, 200 characters, not null)**: The author of the book.
- **synopsis (Text)**: The synopsis of the book.
- **created_at (Date, default: datetime.utcnow)**: The creation date of the record.
- **content (Text, not null)**: The content of the book.

### Usage Examples

1. **Insert a New Book**  
   ```python
   new_book = Books(
       book='Book Title',
       author='Author Name',
       synopsis='Book Synopsis',
       content='Book Content'
   )
   session.add(new_book)
   session.commit()
   ```

2. **Retrieve All Books**  
   ```python
   all_books = session.query(Books).all()
   for book in all_books:
       print(book.serialize())
   ```

3. **Retrieve a Specific Book by ID**  
   ```python
   specific_book = session.query(Books).filter_by(id=1).first()
   print(specific_book.serialize())
   ```

4. **Update an Existing Book**  
   ```python
   book_to_update = session.query(Books).filter_by(id=1).first()
   book_to_update.book = 'New Book Title'
   session.commit()
   ```

5. **Delete a Book by ID**  
   ```python
   book_to_delete = session.query(Books).filter_by(id=1).first()
   session.delete(book_to_delete)
   session.commit()
   ```

### Notes
- Ensure the database connection is properly configured in the SQLAlchemy configuration file.
- Use the `serialize()` function to convert `Books` objects into serialized dictionaries for easier data manipulation.

---