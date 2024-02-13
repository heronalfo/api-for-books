# Application Initialization

This guide provides instructions on how to initialize the book management application.

## Prerequisites

- Python 3.x installed
- Pip (Python package manager) installed
- Virtual environment (optional but recommended)

## Steps

1. **Set Up Virtual Environment (Optional):**
    - It's recommended to set up a virtual environment to isolate the application dependencies. Run the following commands:

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

2. **Install Dependencies:**
    - With the virtual environment activated, install the necessary dependencies by running the following command:

    ```
    pip install -r requirements.txt
    ```

3. **Initialize Database:**
    - Ensure that the SQLite database is properly configured. If not, update the connection URL in the `app.py` file. Then, initialize the database by running the following command:

    ```
    python app.py
    ```

    This will create the SQLite database file specified in the connection URL.

4. **Run Flask Server:**
    - With all dependencies installed and the database initialized, run the following command to start the Flask server:

    ```
    python app.py
    ```

    The Flask server will be available at `http://localhost:5000/`.

5. **Access API:**
    - Once the server is running, you can access the API using the routes defined in `routes.py`. For example:
        - `GET http://localhost:5000/api/books/`: Returns all books.
        - `GET http://localhost:5000/api/books/<id>/`: Returns a specific book by ID.
        - `POST http://localhost:5000/api/books/insert_new_book/`: Inserts a new book.
        - `DELETE http://localhost:5000/api/books/delete_book/<id>/`: Deletes a book by ID.

6. **Deactivate Virtual Environment (Optional):**
    - After finishing the use of the application, you can deactivate the virtual environment using the following command:

    ```
    deactivate
    ```

This concludes the necessary steps to initialize and use the book management application.