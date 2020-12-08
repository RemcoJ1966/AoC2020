from typing import Generator, List
from itertools import chain


def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()

def read_answers() -> Generator[List[str], None, None]:
    answers: List[str] = []
    for line in read_input():
        a = line.rstrip()
        if 0 == len(a):
            yield answers
            answers.clear()
        else:
            answers.append(a)

    yield answers

def amount_anyone_answered_in_group(answers: List[str]) -> int:
    return len(set(chain.from_iterable(answers)))

def amount_all_answered_in_group(answers: List[str]) -> int:
    all_answers = answers[0]
    for i in range(1, len(answers)):
        for a in all_answers:
            if not a in answers[i]:
                all_answers = all_answers.replace(a, '')

    return len(all_answers)


if __name__ == '__main__':
    print(f'Anyone answered: {sum([amount_anyone_answered_in_group(answers) for answers in read_answers()])}')
    print(f'All answered: {sum([amount_all_answered_in_group(answers) for answers in read_answers()])}')

