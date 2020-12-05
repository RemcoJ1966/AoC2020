from typing import Generator, List


def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()

def split_range(rows: List[int], spec: str):
    if 'F' == spec or 'L' == spec:
        return list(range(rows[0], int(len(rows) / 2) + rows[0]))
    else:
        return list(range(int(len(rows) / 2) + rows[0], len(rows) + rows[0]))

def get_seat_id(seat_spec: str) -> int:
    rows = list(range(0, 128))
    for r in range(7):
        rows = split_range(rows, seat_spec[r])

    cols = list(range(0, 8))
    for c in range(7, 10):
        cols = split_range(cols, seat_spec[c])

    return rows[0] * 8 + cols[0]

def get_my_seat_id(seat_id_list: List[int], highest_id: int):
    missing_seats = [s for s in range(highest_id) if s not in seat_id_list]
    
    for seat in missing_seats:
        if seat - 1 in seat_id_list and seat + 1 in seat_id_list:
            return seat
    return -1


if __name__ == '__main__':
    
    seat_id_list = [get_seat_id(i) for i in read_input()]
    highest_id = max(seat_id_list)
    print(f'Seat with highest id: {highest_id}')

    print(f'My seat is {get_my_seat_id(seat_id_list, highest_id)}')