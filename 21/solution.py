from collections import defaultdict
import fileinput
import re
from functools import reduce


def calculate_possible_alergens(food):
    all_ingradients = {ingradient for ingradients,
                       _ in food for ingradient in ingradients}
    possible_alergens = defaultdict(lambda: all_ingradients)
    for ingradients, alergens in food:
        for alergen in alergens:
            possible_alergens[alergen] = possible_alergens[alergen] & set(
                ingradients)
    return possible_alergens, all_ingradients


def get_all_not_alergens(food):
    possible_alergens, all_ingradients = calculate_possible_alergens(food)
    maybe_alergens = reduce(lambda acc, curr: acc | curr,
                            possible_alergens.values(), set())
    return all_ingradients - maybe_alergens


def count_not_alergens_occurences(food):
    not_alergens = get_all_not_alergens(food)
    return sum([ingradient in not_alergens for ingradients, _ in food for ingradient in ingradients])


def map_alergens_to_ingradients(food):
    possible_alergens, all_ingradients = calculate_possible_alergens(food)
    possible_alergens_list = list(possible_alergens.items())
    possible_alergens_list.sort(key=lambda x: len(x[1]))
    mapping = []
    for i, (alergen, ingradients) in enumerate(possible_alergens_list):
        ingradient = ingradients.pop()
        mapping.append((alergen, ingradient))
        for j in range(i, len(possible_alergens_list)):
            if ingradient in possible_alergens_list[j][1]:
                possible_alergens_list[j] = (
                    possible_alergens_list[j][0], possible_alergens_list[j][1] - {ingradient})
        possible_alergens_list.sort(key=lambda x: len(x[1]))
    return mapping


lines = map(lambda x: x.rstrip(), fileinput.input())
matches = map(lambda x: re.match("(.+) \(contains (.+)\)", x), lines)
food = list(map(lambda m: (m.group(1).split(), m.group(2).split(", ")), matches))

# part 1
print(count_not_alergens_occurences(food))

# part 2
print(",".join(map(lambda p: p[1], sorted(
    map_alergens_to_ingradients(food), key=lambda p: p[0]))))
