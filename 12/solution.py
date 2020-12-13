import fileinput

instructions = list(
    map(lambda x: (x[0], int(x.rstrip()[1:])), fileinput.input()))


def manhattan_distance(x, y):
    return abs(x) + abs(y)


def process_instructions_1(instructions):
    facing = 0
    x = 0
    y = 0
    move_forward = {
        0: lambda v: (x + value, y),
        1: lambda v: (x, y + value),
        2: lambda v: (x - value, y),
        3: lambda v: (x, y - value)
    }
    for d, value in instructions:
        if d == 'L':
            facing = (facing + (value // 90)) % 4
        elif d == 'R':
            facing = (facing - (value // 90)) % 4
        elif d == 'F':
            x, y = move_forward[facing](value)
        else:
            x, y = move_forward[['E', 'N', 'W', 'S'].index(d)](value)
    return manhattan_distance(x, y)


def process_instructions_2(instructions):
    x = 0
    y = 0
    waypoint_x = 10
    waypoint_y = 1
    move_forward = {
        0: lambda v: (waypoint_x + value, waypoint_y),
        1: lambda v: (waypoint_x, waypoint_y + value),
        2: lambda v: (waypoint_x - value, waypoint_y),
        3: lambda v: (waypoint_x, waypoint_y - value)
    }
    for d, value in instructions:
        if d == 'L':
            direction = (value // 90)
            if direction == 1:
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
            elif direction == 2:
                waypoint_x, waypoint_y = -waypoint_x, -waypoint_y
            elif direction == 3:
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif d == 'R':
            direction = (value // 90)
            if direction == 1:
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
            elif direction == 2:
                waypoint_x, waypoint_y = -waypoint_x, -waypoint_y
            elif direction == 3:
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        elif d == 'F':
            x = x + value * waypoint_x
            y = y + value * waypoint_y
        else:
            waypoint_x, waypoint_y = move_forward[[
                'E', 'N', 'W', 'S'].index(d)](value)
    return manhattan_distance(x, y)


print(process_instructions_1(instructions))
print(process_instructions_2(instructions))
