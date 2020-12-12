from functools import reduce
import fileinput


def process_position(grid, x, y):
    position_type = grid[x][y]
    if position_type == '.':
        return '.'
    # part 1
    # neighbours = [grid[i][j] for i in range(max(0, x-1), min(len(grid), x+2))
    #               for j in range(max(0, y-1), min(len(grid[0]), y+2)) if i != x or j != y]

    # part 2
    neighbours = []
    steppers = {
        'l': lambda i, j: (i, j-1),
        'r': lambda i, j: (i, j+1),
        'u': lambda i, j: (i+1, j),
        'd': lambda i, j: (i-1, j),
        'ur': lambda i, j: (i+1, j+1),
        'ul': lambda i, j: (i+1, j-1),
        'dr': lambda i, j: (i-1, j+1),
        'dl': lambda i, j: (i-1, j-1)
    }
    for d in steppers.values():
        pos_x, pos_y = d(x, y)
        while (0 <= pos_x < len(grid)) and (0 <= pos_y < len(grid[0])):
            if grid[pos_x][pos_y] != '.':
                neighbours.append(grid[pos_x][pos_y])
                break
            else:
                pos_x, pos_y = d(pos_x, pos_y)
    occupied_neighbours = reduce(
        lambda acc, curr: acc+1 if curr == '#' else acc, neighbours, 0)
    if position_type == 'L':
        return 'L' if occupied_neighbours > 0 else '#'
    if position_type == '#':
        # part 1
        # return '#' if occupied_neighbours < 4 else 'L'

        # part 2
        return '#' if occupied_neighbours < 5 else 'L'


def are_grids_equal(grid_1, grid_2):
    return all(map(lambda i: grid_1[i] == grid_2[i], range(len(grid_1))))


def simulate_step(grid):
    grid_height = len(grid)
    grid_width = len(grid[0])
    new_grid = list(map(lambda _: [''] * grid_width, [''] * grid_height))
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            new_grid[i][j] = process_position(grid, i, j)
    return new_grid


def count_occupied(grid):
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                cnt += 1
    return cnt


grid = list(map(lambda x: list(x.rstrip()), fileinput.input()))
while True:
    new_grid = simulate_step(grid)
    if are_grids_equal(grid, new_grid):
        print(count_occupied(grid))
        break
    else:
        grid = new_grid
