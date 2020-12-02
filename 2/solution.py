from collections import Counter
import fileinput
import re

lines = list(map(lambda x: x.rstrip(), fileinput.input()))
pattern = "(\d+)-(\d+) ([a-z]): ([a-z]+)"
matches = [re.match(pattern, line) for line in lines]
passwords = [match.group(4) for match in matches]
rules = [(int(match.group(1)), int(match.group(2)), match.group(3))
         for match in matches]


def is_valid_1(pair):
    rule, password = pair
    counter = Counter(password)
    return rule[0] <= counter[rule[2]] <= rule[1]


def is_valid_2(pair):
    rule, password = pair
    return (password[rule[0]-1] == rule[2]) != (password[rule[1]-1] == rule[2])


valid_passwords = list(filter(is_valid_2, zip(rules, passwords)))
print(len(valid_passwords))
