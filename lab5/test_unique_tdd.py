import unittest
from unique import Unique


class TestUniqueTDD(unittest.TestCase):
    
    def test_unique_integers(self):
        data = [1, 1, 2, 2, 3, 3, 4, 4]
        result = list(Unique(data))
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_unique_strings_case_sensitive(self):
        data = ['a', 'A', 'b', 'B', 'a', 'A']
        result = list(Unique(data))
        self.assertEqual(result, ['a', 'A', 'b', 'B'])
    
    def test_unique_strings_ignore_case(self):
        data = ['a', 'A', 'b', 'B', 'a', 'A']
        result = list(Unique(data, ignore_case=True))
        self.assertEqual(result, ['a', 'b'])
    
    def test_unique_empty_list(self):
        data = []
        result = list(Unique(data))
        self.assertEqual(result, [])
    
    def test_unique_with_generator(self):
        def gen():
            yield 1
            yield 1
            yield 2
            yield 2
        result = list(Unique(gen()))
        self.assertEqual(result, [1, 2])
    
    def test_unique_preserves_order(self):
        data = [3, 1, 2, 1, 3, 2, 4]
        result = list(Unique(data))
        self.assertEqual(result, [3, 1, 2, 4])
    
    def test_unique_mixed_types(self):
        data = [1, '1', 2, '2', 1, '1']
        result = list(Unique(data))
        self.assertEqual(result, [1, '1', 2, '2'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
