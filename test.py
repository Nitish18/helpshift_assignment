import sys
import os
import unittest
current_dir = os.getcwd()
sys.path.append(current_dir)

from main import execute
from trie_datastructure import Trie


class TestWordSearch(unittest.TestCase):
    """
    Unit test class for word search main.py module.
    """
    def setUp(self):
        self.trie_obj = Trie()

    def test_invalid_user_input(self):
        """
        giving invalid input type.
        """
        res = execute(4, ['Alex'], self.trie_obj)
        correct_res = None
        self.assertEqual(res, correct_res)

    def test_insert_name_success_1(self):
        """
        inserting a valid name into trie.
        here valid name is name whose word length <= 2.
        """
        res = execute(1, ['Chris'], self.trie_obj)
        correct_res = None
        self.assertEqual(res, correct_res)
    
    def test_insert_name_success_2(self):
        """
        inserting a valid name into trie.
        here valid name is name whose word length <= 2.
        """
        res = execute(1, ['Chris', 'Harris'], self.trie_obj)
        correct_res = None
        self.assertEqual(res, correct_res)

    def test_insert_name_fail(self):
        """
        inserting a in-valid name into trie.
        i.e name with more than 2 words in it.
        """
        res = execute(1, ['Chris', 'Harris', 'John'], self.trie_obj)
        correct_res = ["Input name is not valid."]
        self.assertEqual(res, correct_res)

    def test_search_name_success_1(self):
        """
        searching a name in trie which exists in it.
        """

        inserting_name = execute(1, ['John', 'Doe'], self.trie_obj)
        res = execute(2, ['John', 'Doe'], self.trie_obj)
        correct_res = {'John Doe'}
        self.assertEqual(res, correct_res)
    
    def test_search_name_success_2(self):
        """
        searching a name in trie which exists in it.
        """
        inserting_name = execute(1, ['Alex'], self.trie_obj)
        res = execute(2, ['Alex'], self.trie_obj)
        correct_res = {'Alex'}
        self.assertEqual(res, correct_res)

    def test_search_name_fail(self):
        """
        searching a name in trie which does not exists in it.
        """
        inserting_name = execute(1, ['Donald'], self.trie_obj)
        res = execute(2, ['Trump'], self.trie_obj)
        correct_res = set() # empty set
        self.assertEqual(res, correct_res)
    
    
if __name__ == '__main__':
    unittest.main()