import numpy as np
import pandas as pd
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        obj1 = BookLover('Sam', 'xxx@xxx.com', 'Nonfiction')
        obj1.add_book('Book1', 4)
        actual = (obj1.book_list == 'Book1').any().any()
        expected = True
        self.assertEqual(actual, expected, 'Test 1 failed.')
        
    def test_2_add_book(self):
        obj1 = BookLover('Sam', 'xxx@xxx.com', 'Nonfiction')
        obj1.add_book('Book1', 4)
        obj1.add_book('Book1', 4)
        actual = obj1.num_books_read()
        expected = 1
        self.assertEqual(actual, expected, 'Test 2 failed.')
    
    def test_3_has_read(self):
        obj1 = BookLover('Sam', 'xxx@xxx.com', 'Nonfiction')
        obj1.add_book('Book1', 4)
        actual = obj1.has_read('Book1')
        expected = True
        self.assertEqual(actual, expected, 'Test 3 failed.')

    def test_4_has_read(self):
        obj1 = BookLover('Sam', 'xxx@xxx.com', 'Nonfiction')
        actual = obj1.has_read('Book1')
        self.assertFalse(actual, 'Test 4 failed.')

    def test_5_num_books_read(self):
        obj1 = BookLover('Sam', 'xxx@xxx.com', 'Nonfiction')
        obj1.add_book('Book1', 4)
        obj1.add_book('Book2', 3)
        actual = obj1.num_books
        expected = len(obj1.book_list)
        self.assertEqual(actual, expected, 'Test 5 failed.')
        
    def test_6_fav_books(self):
        obj1 = BookLover('Sam', 'xxx@xxx.com', 'Nonfiction')
        obj1.add_book('Book1', 4)
        obj1.add_book('Book2', 3)
        obj1.add_book('Book3', 2)
        favs = obj1.fav_books()
        less_than_3 = favs[favs['book_rating'] <= 3]
        actual = len(less_than_3)
        expected = 0
        self.assertEqual(actual, expected, 'Test 6 failed.')

        
if __name__ == '__main__':
    unittest.main(verbosity=3)

