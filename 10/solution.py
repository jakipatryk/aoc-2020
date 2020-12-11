import fileinput
from functools import reduce
from collections import defaultdict
from itertools import dropwhile

lines = list(map(lambda x: int(x.rstrip()), fileinput.input()))

lines.sort()

# part 1


def update_dict(d, key, value):
    d[key] = value
    return d


differences = reduce(lambda acc, curr: update_dict(
    acc, curr[1] - curr[0], acc[curr[1] - curr[0]] + 1), zip([0] + lines, lines + [max(lines) + 3]), defaultdict(int))

print(differences[3] * differences[1])


# part 2


def count_paths():
    memo = [0] * (max(lines) + 1)
    memo[0] = 1
    memo[1] = 1 if (lines[1] - lines[0]) <= 3 else 0
    memo[2] = 2 if (lines[2] - lines[0]) <= 3 else 1
    for n in dropwhile(lambda x: x <= 2, lines):
        memo[n] = memo[n-3] + memo[n-2] + memo[n-1]
    return memo[max(lines)]


print(count_paths())
