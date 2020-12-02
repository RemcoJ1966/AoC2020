import unittest
from day1 import fix_expense_report, fix_expense_report3


class TestDay1(unittest.TestCase):

    def test_fix_expense_report(self):
        report = [1721, 979, 366, 299, 675, 1456]
        expected = 514579
        self.assertEqual(expected, fix_expense_report(report))

    def test_fix_expense_report3(self):
        report = [1721, 979, 366, 299, 675, 1456]
        expected = 241861950
        self.assertEqual(expected, fix_expense_report3(report))

if __name__ == '__main__':
    unittest.main()