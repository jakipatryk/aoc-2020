import fileinput

# part 1
entries = list(map(lambda x: int(x.rstrip()), fileinput.input()))
entries_set = set()
for entry in entries:
    needed = 2020 - entry
    if needed in entries_set:
        print(entry * needed)
        break
    entries_set.add(entry)

# part 2
sum_of_two = {a+b: ({a, b}, a*b)
              for a in entries_set for b in entries_set if a != b}
for entry in entries:
    needed = 2020 - entry
    if needed in sum_of_two and not {entry} <= sum_of_two[needed][0]:
        print(entry * sum_of_two[needed][1])
        break
