from typing import Deque, Generator, List
from itertools import combinations


def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()

def find_first(numbers: List[int]) -> int:
    q = Deque((), 25)
    i = 0
    for number in numbers:
        if i >= 25:
            combos = combinations(q, 2)
            sums = set([x + y for x, y in combos])
            if number not in sums:
                return number

        q.append(number)
        i += 1

    return 0

def find_weakness(numbers: List[int], first: int) -> int:
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            nos = numbers[i:j]
            if first == sum(nos):
                return min(nos) + max(nos)

    return 0

if __name__ == '__main__':

    numbers = [int(line.rstrip()) for line in read_input()]

    first = find_first(numbers)
    print(f'The first number is {first}')

    # numbers = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    # first = 127
    print(f'The weakness is {find_weakness(numbers, first)}')

