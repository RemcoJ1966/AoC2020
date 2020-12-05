import unittest
from day5 import get_seat_id


param_list = [
    ('FBFBBFFRLR', 357),
    ('BFFFBBFRRR', 567),
    ('FFFBBBFRRR', 119),
    ('BBFFBBFRLL', 820)
]

class TestDay5(unittest.TestCase):

    def test_get_seat_id(self):
        for t in param_list:
            with self.subTest(t[0]):
                self.assertEqual(t[1], get_seat_id(t[0]))


if __name__ == '__main__':
    unittest.main()