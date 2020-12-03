import unittest
from day3 import count_trees


param_list = [
    (1, 1, 2),
    (3, 1, 7),
    (5, 1, 3),
    (7, 1, 4),
    (1, 2, 2)
]

class TestDay3(unittest.TestCase):

    def test_area(self):
        area = [
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#'
        ]
        for t in param_list:
            with self.subTest():
                self.assertEqual(t[2], count_trees(area, t[0], t[1]))


if __name__ == '__main__':
    unittest.main()