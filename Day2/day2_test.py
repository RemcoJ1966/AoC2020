import unittest
from day2 import password_is_valid, password_is_valid_2

param_list = [
    (1, 3, 'a', 'abcde', True),
    (1, 3, 'b', 'cdefg', False),
    (2, 9, 'c', 'ccccccccc', True)
]

param_list_2 = [
    (1, 3, 'a', 'abcde', True),
    (1, 3, 'b', 'cdefg', False),
    (2, 9, 'c', 'ccccccccc', False)
]

class TestDay2(unittest.TestCase):

    def test_password_valid(self):
        for t in param_list:
            with self.subTest(t[0]):
                self.assertEqual(password_is_valid(t[0], t[1], t[2], t[3]), t[4])

    def test_password_valid_2(self):
        for t in param_list_2:
            with self.subTest(t[0]):
                self.assertEqual(password_is_valid_2(t[0], t[1], t[2], t[3]), t[4])

if __name__ == '__main__':
    unittest.main()
