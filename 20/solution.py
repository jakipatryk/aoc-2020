from itertools import product
import fileinput
from functools import reduce
from operator import mul
from collections import defaultdict


def get_borders(tile):
    height, width = len(tile), len(tile[1])
    borders = []
    borders.append([row[width - 1] for row in tile])
    borders.append(tile[height - 1])
    borders.append([row[0] for row in tile])
    borders.append(tile[0])
    return borders


def get_possible_neighbours(tile, tiles):
    tile_id, tile_image = tile
    tile_borders = get_borders(tile_image)
    possibilities = []
    for nb_id, nb_image in tiles:
        if nb_id == tile_id:
            continue
        nb_borders = get_borders(nb_image)
        for (i, bd_1), (j, bd_2) in product(enumerate(tile_borders), enumerate(nb_borders)):
            if bd_1 == bd_2:
                possibilities.append(
                    (tile_id,
                     nb_id,
                     i,
                     j,
                     "NOT_REVERSED")
                )
            elif bd_1 == list(reversed(bd_2)):
                possibilities.append(
                    (tile_id,
                     nb_id,
                     i,
                     j,
                     "REVERSED")
                )
    return possibilities


# def arange_tiles(tiles, possibilities):
#     # tile_id: (edge_number_on_right, edge_number_on_down, [nb_ids])
#     descriptions = defaultdict(list)
#     # corner_ids = list(
#     #     map(lambda nb: nb[0][0], filter(lambda nb: len(nb) == 2, nbs)))
#     grid = [[-1 for j in range(12)] for i in range(12)]
#     grid[0][0] = (3557, 0, 1)
#     for level in range(1, 12):

#         for i in range(1, level - 1):
#             y = level - i
#             x = i
#             left = grid[y][x - 1]
#             up = grid[y - 1][x]
#             left_desc = next(
#                 k for k in possibilities if k[0][0] == left[0])
#             left_edge_number_on_right = left[1]
#             current_number_on_left = next(
#                 k[3] for k in left_desc if k[2] == left_edge_number_on_right)
#             current_id = next(k[1] for k in left_desc if k[2]
#                                 == left_edge_number_on_right)
#             up_desc = next(k for k in possibilities if k[0][0] == up[0])
#             up_edge_number_on_down = up[2]
#             current_number_on_up = next(
#                 k[3] for k in up_desc if k[2] == up_edge_number_on_down)
#             current_id = next(k[1] for k in up_desc if k[2]
#                                 == up_edge_number_on_down)
#             if current_number_on_up == (current_number_on_left + 1) or (current_number_on_left == 3 and current_number_on_up == 0):
#                 current_number_on_down = (current_number_on_up + 2) % 4
#                 current_number_on_right = (current_number_on_left + 2) % 4
#             else:
#                 current_number_on_down = (current_number_on_left + 2) % 4
#                 current_number_on_right = (current_number_on_up + 2) % 4
#             grid[level - i][i] = (current_id,
#                                   current_number_on_right, current_number_on_down)
#     return grid


lines = list(map(lambda x: x.rstrip(), fileinput.input()))
tiles = [lines[i:(i+11)] for i in range(0, len(lines), 12)]
tiles = list(map(lambda t: (int(t[0][5:9]), list(map(list, t[1:]))), tiles))
nbs = list(map(lambda t: get_possible_neighbours(t, tiles), tiles))

# part 1
print(reduce(mul, map(lambda nb: nb[0][0],
                      filter(lambda nb: len(nb) == 2, nbs)), 1))

# part 2
# DIDN'T SOLVE :(
