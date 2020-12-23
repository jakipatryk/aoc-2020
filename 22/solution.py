from collections import deque, defaultdict
from functools import reduce
import fileinput


def play_round(a_deck: deque, b_deck: deque, decision_function, memo: defaultdict):
    if memo[str(a_deck) + "," + str(b_deck)]:
        return 1
    memo[str(a_deck) + "," + str(b_deck)] = True
    a_top = a_deck.popleft()
    b_top = b_deck.popleft()
    if decision_function(a_top, b_top, a_deck, b_deck, memo) == 1:
        a_deck.append(a_top)
        a_deck.append(b_top)
    else:
        b_deck.append(b_top)
        b_deck.append(a_top)

    if len(a_deck) == 0:
        return 2
    elif len(b_deck) == 0:
        return 1
    else:
        return 0


def calculate_score(deck: deque):
    return reduce(lambda acc, curr: acc + (1 + curr[0]) * curr[1], enumerate(reversed(deck)), 0)


def simulate_game(a_deck: deque, b_deck: deque, decision_function, memo: set):
    while True:
        winner = play_round(a_deck, b_deck, decision_function, memo)
        if winner != 0:
            break
    return winner


def decision_function_1(a_top, b_top, a_deck, b_deck, memo):
    return a_top > b_top


def decision_function_2(a_top, b_top, a_deck, b_deck, memo):
    if a_top > len(a_deck) or b_top > len(b_deck):
        return a_top > b_top
    else:
        a_cpy = deque(list(a_deck)[:a_top])
        b_cpy = deque(list(b_deck)[:b_top])
        return simulate_game(a_cpy, b_cpy, decision_function_2, defaultdict(bool)) == 1


lines = list(map(lambda x: x.rstrip(), fileinput.input()))
player_1 = deque(map(int, lines[1:26]))
player_2 = deque(map(int, lines[28:]))

# part 1
player_1_deck = player_1.copy()
player_2_deck = player_2.copy()
winner = simulate_game(
    player_1_deck, player_2_deck, decision_function_1, defaultdict(bool))
print(calculate_score(player_1_deck if winner == 1 else player_2_deck))

# part 2
player_1_deck = player_1.copy()
player_2_deck = player_2.copy()
winner = simulate_game(
    player_1_deck, player_2_deck, decision_function_2, defaultdict(bool))
print(calculate_score(player_1_deck if winner == 1 else player_2_deck))
