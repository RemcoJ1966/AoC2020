from typing import List


Area = List[str]

def count_trees(area: Area, r: int, d: int) -> int:
    l = len(area)
    w = len(area[0])
    
    trees = 0
    for y in range(0, l, d):
        x = int((y/d * r) % w)
        if '#' == area[y][x]:
            trees += 1

    return trees

if __name__ == '__main__':

    area = []

    with open('input', 'r') as f:
        line = f.readline()
        while line:
            area.append(line.strip())
            line = f.readline()

    print(f'Number of trees is {count_trees(area, 3, 1)}')

    print(f"""Number of trees 2 is 
        {count_trees(area, 1, 1) *
        count_trees(area, 3, 1) *
        count_trees(area, 5, 1) *
        count_trees(area, 7, 1) *
        count_trees(area, 1, 2)}""")
