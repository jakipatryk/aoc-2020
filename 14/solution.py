import re
import fileinput


def decompose_bitmask_1(mask):
    mask_super = int(
        "".join(list(map(lambda x: '0' if x == 'X' else x, mask))), 2)
    mask_and = int(
        "".join(list(map(lambda x: '1' if x == 'X' else '0', mask))), 2)
    return mask_super, mask_and


def apply_mask(value, mask_super, mask_and):
    return mask_super | (value & mask_and)


def process_instructions_1(instructions):
    memory = {}
    for action, value in instructions:
        if action == "mask":
            mask_super, mask_and = decompose_bitmask_1(value)
        else:
            address = re.match("mem\[(\d+)\]", action).group(1)
            memory[address] = apply_mask(int(value), mask_super, mask_and)
    return sum(memory.values())


def generate_all_addresses(mask, address):
    if not mask:
        yield 0
    else:
        if mask[~0] == '0':
            for a in generate_all_addresses(mask[:~0], address >> 1):
                yield (a << 1) | (address & 1)
        if mask[~0] == '1':
            for a in generate_all_addresses(mask[:~0], address >> 1):
                yield (a << 1) | 1
        if mask[~0] == 'X':
            for a in generate_all_addresses(mask[:~0], address >> 1):
                yield (a << 1)
                yield (a << 1) | 1


def process_instructions_2(instructions):
    memory = {}
    for action, value in instructions:
        if action == "mask":
            mask = value
        else:
            address = int(re.match("mem\[(\d+)\]", action).group(1))
            for a in generate_all_addresses(mask, address):
                memory[a] = int(value)
    return sum(memory.values())


instructions = list(map(lambda x: x.rstrip().split(" = "), fileinput.input()))

# part 1
print(process_instructions_1(instructions))

# part 2
print(process_instructions_2(instructions))
