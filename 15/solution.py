import fileinput


def get_nth_number(start, n):
    prev_occurences = {}
    for i, num in enumerate(start[:-1]):
        prev_occurences[num] = i
    prev = start[~0]
    for j in range(len(start), n):
        num = 0 if prev not in prev_occurences else (
            j - prev_occurences[prev] - 1)
        prev_occurences[prev] = j - 1
        prev = num
    return prev


start = list(
    map(lambda x: list(map(int, x.rstrip().split(","))), fileinput.input()))[0]

print(get_nth_number(start, 2020))
print(get_nth_number(start, 30000000))
