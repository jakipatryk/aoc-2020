def get_three_next_cups(cups, before):
    fst = cups[before]
    snd = cups[fst]
    trd = cups[snd]
    return [fst, snd, trd]


def swap_cyclic(next_clockwise_cups, cups, destination, current_cup):
    cups[current_cup] = cups[next_clockwise_cups[2]]
    cups[next_clockwise_cups[2]] = cups[destination]
    cups[destination] = next_clockwise_cups[0]


def get_destination(cups, current_cup, next_clockwise_cups, mod):
    n = mod if current_cup == 1 else (current_cup - 1)
    while n in next_clockwise_cups:
        n = mod if n == 1 else (n - 1)
    return n


def simulate_move(cups, current_cup, mod):
    next_clockwise_cups = get_three_next_cups(cups, current_cup)
    destination = get_destination(cups, current_cup, next_clockwise_cups, mod)
    swap_cyclic(next_clockwise_cups, cups, destination, current_cup)
    return cups[current_cup]


def simulate(cups, current_cup, n=100, mod=9):
    for _ in range(n):
        current_cup = simulate_move(cups, current_cup, mod)
    return cups


def print_answer(cups):
    as_str = ""
    n = cups[1]
    while n != 1:
        as_str += str(n)
        n = cups[n]
    return as_str


# part 1
cups_order = [1, 3, 7, 8, 2, 6, 4, 9, 5]
cups = [-1, 3, 6, 7, 9, 1, 4, 8, 2, 5]
print(print_answer(simulate(cups, cups_order[0])))

# part 2
cups = [-1, 3, 6, 7, 9, 10, 4, 8, 2, 5] + list(range(11, 1000001)) + [1]
ans = simulate(cups, cups_order[0], 10000000, 1000000)
print(ans[1] * ans[ans[1]])
