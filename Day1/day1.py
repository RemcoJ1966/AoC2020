from itertools import combinations
from typing import List

def fix_expense_report(report: List[int]) -> int :
    v = [(x, y) for x, y in combinations(report, 2) if 2020 == x + y]
    x, y = v[0]
    return x * y

def fix_expense_report3(report: List[int]) -> int :
    v = [(x, y, z) for x, y, z in combinations(report, 3) if 2020 == x + y + z]
    x, y, z = v[0]
    return x * y * z


if __name__ == '__main__':

    report = []

    with open('input', 'r') as f:
        line = f.readline()
        while line:
            report.append(int(line))
            line = f.readline()

    print(f'Result 2 is {fix_expense_report(report)}')
    print(f'Result 3 is {fix_expense_report3(report)}')
 