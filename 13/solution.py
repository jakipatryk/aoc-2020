import fileinput

lines = list(map(lambda x: x.rstrip(), fileinput.input()))

# part 1
earliest_depart = int(lines[0])
buses_ids = map(lambda id: int(id), filter(
    lambda x: x != 'x', lines[1].split(',')))
buses = list(map(lambda id: (id, id - (earliest_depart % id)), buses_ids))
earliest_bus = min(buses, key=lambda p: p[1])
print(earliest_bus[0] * earliest_bus[1])

# part 2


def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def combine_buses(a, b):
    gcd, s, t = extended_gcd(a[1], b[1])
    n = ((a[0] - b[0]) // gcd) * s
    m = -((a[0] - b[0]) // gcd) * t
    combined_translation = a[0] - n * a[1]
    combined_peroid = (a[1] * b[1]) // gcd
    return (combined_translation % combined_peroid, combined_peroid)


def find_timestamp(buses):
    peroid = int(buses[0])
    translation = 0
    for i in range(1, len(buses)):
        if buses[i] != 'x':
            translation, peroid = combine_buses(
                (translation, peroid), (-i, int(buses[i])))
    return translation


print(find_timestamp(lines[1].split(',')))
