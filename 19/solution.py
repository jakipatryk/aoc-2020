from itertools import product
import fileinput
import re


def is_in_language(grammar, w):
    X = [[[n for n, prod in grammar if prod[0][0] ==
           f'"{a}"' or (len(prod) > 1 and prod[1][0] == f'"{a}"')] for i, a in enumerate(w)]]
    for i in range(1, len(w)):
        X.append([])
        for j in range(len(w) - i):
            X[i].append([])
            for k in range(j + 1, j + (i + 1)):
                X[i][j] = X[i][j] + [n for A, B in product(
                    X[k - j - 1][j], X[i - (k - j)][k]) for n, prod in grammar if [A, B] in prod]
    return '0' in X[len(w) - 1][0]


# part 1
# # Before running the script, remove unit productions on input grammar by hand.
# lines = list(map(lambda x: x.rstrip(), fileinput.input()))
# grammar = lines[:135]
# grammar = map(lambda l: re.match("(\d+): (.+)", l), grammar)
# grammar = list(map(lambda m: (m.group(1), list(
#     map(lambda x: x.split(), m.group(2).split(" | ")))), grammar))
# words = lines[136:]
# print(sum(map(lambda w: is_in_language(grammar, w), words)))

# part 2
# Before running the script, remove unit productions
# and get input grammar to Chomsky Normal Form by hand.
lines = list(map(lambda x: x.rstrip(), fileinput.input()))
grammar = lines[:136]
grammar = map(lambda l: re.match("(\d+): (.+)", l), grammar)
grammar = list(map(lambda m: (m.group(1), list(
    map(lambda x: x.split(), m.group(2).split(" | ")))), grammar))
words = lines[137:]
print(sum(map(lambda w: is_in_language(grammar, w), words)))
