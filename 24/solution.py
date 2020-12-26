from collections import defaultdict
import fileinput


def parse_position(position: str):
    position_on_grid = (0, 0)
    updaters = {
        'e': lambda pos, i: ((pos[0] + 1, pos[1]), i + 1),
        'w': lambda pos, i: ((pos[0] - 1, pos[1]), i + 1),
        's': lambda pos, i: ((pos[0] + 1 if pos[1] % 2 == 0 else pos[0], pos[1] + 1), i + 2) if position[i + 1] == 'e' else ((pos[0] if pos[1] % 2 == 0 else pos[0] - 1, pos[1] + 1), i + 2),
        'n': lambda pos, i: ((pos[0] + 1 if pos[1] % 2 == 0 else pos[0], pos[1] - 1), i + 2) if position[i + 1] == 'e' else ((pos[0] if pos[1] % 2 == 0 else pos[0] - 1, pos[1] - 1), i + 2)
    }
    i = 0
    while i < len(position):
        c = position[i]
        position_on_grid, i = updaters[c](position_on_grid, i)
    return position_on_grid


def grid_to_matrix(grid):
    min_x = min(grid.keys(), key=lambda x: x[0])[0]
    min_y = min(grid.keys(), key=lambda x: x[1])[1]
    max_x = max(grid.keys(), key=lambda x: x[0])[0]
    max_y = max(grid.keys(), key=lambda x: x[1])[1]
    return [[grid[(i + min_x, j + min_y)] for j in range(max_y - min_y + 1)] for i in range(max_x - min_x + 1)], min_x, max_x, min_y, max_y


def simulate_days(matrix, min_x, max_x, min_y, max_y, n=100):
    for _ in range(n):
        height = len(matrix)
        width = len(matrix[0])
        matrix = [[0 for _ in range(width + 4)] for i in range(2)] + [[0, 0] + row + [0, 0]
                                                                      for row in matrix] + [[0 for _ in range(width + 4)] for i in range(2)]
        new_mtx = [[0 for j in range(width + 4)] for i in range(height + 4)]
        min_x -= 2
        min_y -= 2
        max_x += 2
        max_y += 2
        for i in range(1, width + 3):
            for j in range(1, height + 3):
                new_mtx[i][j] = matrix[i][j]
                if (j + min_y) % 2 == 0:
                    nbs = [(i - 1, j), (i + 1, j), (i, j + 1),
                           (i, j - 1), (i + 1, j - 1), (i + 1, j + 1)]
                else:
                    nbs = [(i - 1, j), (i + 1, j), (i, j - 1),
                           (i, j + 1), (i - 1, j + 1), (i - 1, j - 1)]
                nbs = map(lambda p: matrix[p[0]][p[1]], nbs)
                nbs_sum = sum(nbs)
                if matrix[i][j] == 1 and (nbs_sum == 0 or nbs_sum > 2):
                    new_mtx[i][j] = 0
                elif matrix[i][j] == 0 and nbs_sum == 2:
                    new_mtx[i][j] = 1
        matrix = new_mtx
    return matrix


def sum_matrix(matrix):
    return sum(map(sum, matrix))


lines = list(map(lambda x: x.rstrip(), fileinput.input()))

# part 1
grid = defaultdict(int)
for l in lines:
    pos = parse_position(l)
    grid[pos] = (grid[pos] + 1) % 2
print(sum(grid.values()))

# part 2
mtx, min_x, max_x, min_y, max_y = grid_to_matrix(grid)
print(sum_matrix(simulate_days(mtx, min_x, max_x, min_y, max_y)))
