import unittest
from unittest.mock import Mock, MagicMock, patch
from unique import Unique


class TestUniqueWithMocks(unittest.TestCase):
    
    def test_unique_with_mock_iterator(self):
        mock_iterator = Mock()
        mock_iterator.__iter__ = Mock(return_value=iter([1, 1, 2, 2, 3]))
        result = list(Unique(mock_iterator))
        self.assertEqual(result, [1, 2, 3])
    
    def test_unique_calls_next_on_items(self):
        data = [1, 2, 3]
        unique_obj = Unique(data)
        with patch.object(unique_obj, 'items') as mock_items:
            mock_items.__next__ = Mock(side_effect=[1, 2, 3, StopIteration])
            try:
                while True:
                    next(unique_obj)
            except StopIteration:
                pass
            self.assertTrue(mock_items.__next__.called)
    
    def test_unique_with_mock_data_source(self):
        mock_data_source = MagicMock()
        mock_data_source.__iter__.return_value = iter(['x', 'y', 'x', 'z'])
        result = list(Unique(mock_data_source))
        self.assertEqual(result, ['x', 'y', 'z'])
        mock_data_source.__iter__.assert_called_once()


if __name__ == '__main__':
    unittest.main(verbosity=2)
