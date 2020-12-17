from collections import defaultdict
import fileinput


def simulate_n_steps_3D(grid, n):
    grid3D = defaultdict(int)
    boundary = [(0, len(grid)), (0, len(grid[0])), (0, 1)]
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            grid3D[(i, j, 0)] = 1 if el == '#' else 0
    for _ in range(n):
        new_grid3D = grid3D.copy()
        for i, (l, r) in enumerate(boundary):
            boundary[i] = (l-1, r+1)
        for y in range(*boundary[0]):
            for x in range(*boundary[1]):
                for z in range(*boundary[2]):
                    nb = [grid3D[(i, j, l)] for i in range(y-1, y+2) for j in range(
                        x-1, x+2) for l in range(z-1, z+2) if {i-y, j-x, l-z} != {0}]
                    if grid3D[(y, x, z)] == 1 and not ({sum(nb)} <= {2, 3}):
                        new_grid3D[(y, x, z)] = 0
                    elif grid3D[(y, x, z)] == 0 and sum(nb) == 3:
                        new_grid3D[(y, x, z)] = 1
        grid3D = new_grid3D
    return sum(grid3D.values())


def simulate_n_steps_4D(grid, n):
    grid4D = defaultdict(int)
    boundary = [(0, len(grid)), (0, len(grid[0])), (0, 1), (0, 1)]
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            grid4D[(i, j, 0, 0)] = 1 if el == '#' else 0
    for _ in range(n):
        new_grid4D = grid4D.copy()
        for i, (l, r) in enumerate(boundary):
            boundary[i] = (l-1, r+1)
        for y in range(*boundary[0]):
            for x in range(*boundary[1]):
                for z in range(*boundary[2]):
                    for k in range(*boundary[3]):
                        nb = [
                            grid4D[(i, j, l, o)]
                            for i in range(y-1, y+2)
                            for j in range(x-1, x+2)
                            for l in range(z-1, z+2)
                            for o in range(k-1, k+2)
                            if {i-y, j-x, l-z, o-k} != {0}
                        ]
                        if grid4D[(y, x, z, k)] == 1 and not ({sum(nb)} <= {2, 3}):
                            new_grid4D[(y, x, z, k)] = 0
                        elif grid4D[(y, x, z, k)] == 0 and sum(nb) == 3:
                            new_grid4D[(y, x, z, k)] = 1
        grid4D = new_grid4D
    return sum(grid4D.values())


grid = list(map(lambda x: list(x.rstrip()), fileinput.input()))

# part 1
print(simulate_n_steps_3D(grid, 6))

# part 2
print(simulate_n_steps_4D(grid, 6))
