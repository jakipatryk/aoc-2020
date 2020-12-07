import fileinput
from functools import reduce
import string


def load_group_yes_answers():
    yes_answers = []
    lines = fileinput.input()
    answer = ''
    for l in lines:
        if l == '\n':
            yes_answers.append(answer)
            answer = ''
        else:
            answer += " " + l.rstrip()
    yes_answers.append(answer)
    return map(lambda p: p.rstrip().lstrip(), yes_answers)


yes_answers = list(load_group_yes_answers())
# part 1
print(sum(map(lambda a: len(set(a.replace(" ", ""))), yes_answers)))

# part 2
print(sum(map(lambda a: len(reduce(lambda acc, curr: set(curr) &
                                   acc, a.split(), set(string.ascii_lowercase))), yes_answers)))
