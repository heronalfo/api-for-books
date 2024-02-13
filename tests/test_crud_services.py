import ..app
import json
import unittest

class CrudServicesTests(unittest.TestCase):

    def setUp(self):
    
        self.app = app.app.test_client()
        self.app.testing = True
        
        self.book = {
        "book": 'Pessoas criativas são mais felizes e ganham mais',
        "author": 'Alexandre felício',
        "synopsis": 'Com este livro, você aprenderá a libertar a sua criatividade independente de sua idade.',
        "content": 'Teste'
    }
    
        self.id = 1
    
    def test_get_all_books(self):
    
        response = self.app.get('/api/books/')
        
        self.assertEqual(response.status_code,  200)
        
    def test_get_all_book_by_id(self):
    
        response = self.app.get('/api/books/1/')
        
        self.assertEqual(response.status_code,  200)
   
    def test_insert_new_book(self):
        
        with self.assertRaises(Exception) as context:
            
            response = self.app.post('/api/books/insert_new_book/', data=json.dumps(self.book))
            
            self.assertEqual(response.status_code, 200)
        
        exception = context.exception
        
        print(exception.__traceback__)
    
    def test_delete_book(self):
        
        with self.assertRaises(Exception) as context:
            
            response = self.app.post('/api/books/delete_book/', data=json.dumps(self.id))
            
            self.assertEqual(response.status_code, 200)
        
        exception = context.exception
        
        print(exception.__traceback__)
    
    def edit_book(self):
        
        with self.assertRaises(Exception) as context:
            
            response = self.app.patch('/api/books/edit_book/', data=json.dumps(self.id))
            
            self.assertEqual(response.status_code, 200)
        
        exception = context.exception
        
        print(exception.__traceback__)
       

if __name__ == '__main__':
    
    unittest.main()