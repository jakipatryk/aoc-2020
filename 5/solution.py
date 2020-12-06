import fileinput


def calculate_row_and_column(boarding_pass: str):
    row_actions = boarding_pass[:7]
    col_actions = boarding_pass[7:]
    row_start = 0
    row_end = 128
    col_start = 0
    col_end = 8
    for action in row_actions:
        m = (row_start + row_end) // 2
        if action == 'F':
            row_end = m
        elif action == 'B':
            row_start = m
    for action in col_actions:
        m = (col_start + col_end) // 2
        if action == 'L':
            col_end = m
        elif action == 'R':
            col_start = m
    return (row_start, col_start)


def calculate_seat_ID(row: int, col: int):
    return 8*row+col


boarding_passes = list(map(lambda x: x.rstrip(), fileinput.input()))
ids = list(map(lambda bp: calculate_seat_ID(
    *calculate_row_and_column(bp)), boarding_passes))

# part 1
print(max(ids))

# part 2
ids.sort()
for id_1, id_2 in zip(ids[1:], ids[2:]):
    if id_2 != id_1 + 1:
        print(id_2-1)
        break
