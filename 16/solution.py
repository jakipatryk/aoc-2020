import fileinput
import re
from functools import reduce


def sum_all_invalid_and_remove(fields, tickets):
    s = 0
    valid = []
    for i, ticket in enumerate(tickets):
        all_good = True
        for v in ticket:
            for _, l1, r1, l2, r2 in fields:
                if (l1 <= v <= r1) or (l2 <= v <= r2):
                    break
            else:
                all_good = False
                s += v
        if all_good:
            valid.append(ticket)
    return (s, valid)


def find_all_possible(fields, tickets):
    possible = []
    for i in range(len(fields)):
        possible.append([])
        for name, l1, r1, l2, r2 in fields:
            for j in range(len(tickets)):
                if not ((l1 <= tickets[j][i] <= r1) or (l2 <= tickets[j][i] <= r2)):
                    break
            else:
                possible[i].append(name)
    return possible


lines = list(map(lambda x: x.rstrip(), fileinput.input()))
fields = map(lambda l: re.match(
    "(.+): (\d+)-(\d+) or (\d+)-(\d+)", l), lines[:20])
fields = list(map(lambda m: (m.group(1), int(m.group(2)),
                             int(m.group(3)), int(m.group(4)), int(m.group(5))), fields))
my_ticket = list(map(int, lines[22].split(",")))
nearby_tickets = list(map(lambda l: list(map(int, l.split(","))), lines[25:]))

# part 1
s, valid_tickets = sum_all_invalid_and_remove(fields, nearby_tickets)
print(s)

# part 2
possible = find_all_possible(fields, valid_tickets)
possible = list(enumerate(possible))
possible.sort(key=lambda p: len(p[1]))
prev = set()
mult = 1
for i, p in possible:
    if list((set(p) - prev))[0].startswith("departure"):
        mult *= my_ticket[i]
    prev = set(p)
print(mult)
