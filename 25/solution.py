def determine_priv_key(pub_key, mod, subject_number=7):
    value = 1
    i = 0
    while True:
        i += 1
        value *= subject_number
        value = value % mod
        if value == pub_key:
            return i


def calculate_encryption_key(one_priv_key, other_pub_key, mod):
    val = 1
    for _ in range(one_priv_key):
        val *= other_pub_key
        val = val % mod
    return val


card_pub_key = 11404017
door_pub_key = 13768789
mod = 20201227
card_priv_key = determine_priv_key(card_pub_key, mod)
door_priv_key = determine_priv_key(door_pub_key, mod)
print(calculate_encryption_key(card_priv_key, door_pub_key, mod))
