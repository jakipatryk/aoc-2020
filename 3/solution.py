from collections import Counter
import fileinput
import re
import operator
from functools import reduce

grid = list(map(lambda x: x.rstrip(), fileinput.input()))
height = len(grid)


def find_number_of_trees_along_path(step):
    position = (0, 0)
    trees_along_path = 0
    while position[0] < height:
        position = tuple(map(operator.add, position, step))
        if position[1] >= len(grid[0]):
            position = (position[0], position[1] % len(grid[0]))
        if position[0] < height and grid[position[0]][position[1]] == '#':
            trees_along_path += 1
    return trees_along_path


slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
print(reduce(operator.mul, map(find_number_of_trees_along_path, slopes), 1))
