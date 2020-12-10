import fileinput

lines = list(map(lambda x: int(x.rstrip()), fileinput.input()))


def find_first_wrong():
    for i in range(25, len(lines)):
        preamble = lines[(i-25):i]
        sums = {a + b for a in preamble for b in preamble if a != b}
        if lines[i] not in sums:
            return lines[i]


def find_consecutive_subarray(sum_to):
    current_sum = lines[0]
    i = 0
    j = 1
    while j < len(lines):
        if current_sum == sum_to:
            return lines[i:j]
        elif current_sum < sum_to:
            current_sum += lines[j]
            j += 1
        else:
            current_sum -= lines[i]
            i += 1


# part 1
wrong_value = find_first_wrong()
print(wrong_value)

# part 2
subarr = find_consecutive_subarray(wrong_value)
print(min(subarr) + max(subarr))
