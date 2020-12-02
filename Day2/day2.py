from typing import Generator, List

def password_is_valid(min: int, max: int, letter: str, pw: str) -> bool:
    return min <= pw.count(letter) <= max

def password_is_valid_2(min: int, max: int, letter: str, pw: str) -> bool:
    pos1 = letter == pw[min - 1]
    pos2 = letter == pw[max - 1]
    return pos1 ^ pos2

def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()

def min_max(s: str) -> List[str]:
    return s.split('-')


if __name__ == '__main__':

    valid = 0
    valid_2 = 0
    for x in (v.split() for v in read_input()):
        min, max = min_max(x[0])
        if password_is_valid(int(min), int(max), x[1][0], x[2]):
            valid += 1
        if password_is_valid_2(int(min), int(max), x[1][0], x[2]):
            valid_2 += 1

    print(f'Number of valid passwords: {valid}')
    print(f'Number of valid passwords 2: {valid_2}')
 