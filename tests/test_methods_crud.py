import ..app
import unittest

class MethodsCrudTest(unittest.TestCase):
    
    def setUp(self):
        
        self.app = app.app.test_client()
        self.app.testing = True
    
    def test_method_get_all_book_is_correct(self):
        
        response = self.app.post('/api/books/')
        
        self.assertEqual(response.status_code, 405)
        
   
    def test_method_get_all_book_by_id_is_correct(self):
        
        response = self.app.post('/api/books/1/')
        
        self.assertEqual(response.status_code,  405)
        
    def test_method_insert_new_book_is_correct(self):
        
        response = self.app.get('/api/books/insert_new_book/')
        
        self.assertEqual(response.status_code,  405)
    
    def test_method_edit_book_is_correct(self):
        
        response = self.app.get('/api/books/edit_book/')
        
        self.assertEqual(response.status_code,  405)

if __name__ == '__main__':
    
    unittest.main()