import fileinput
import re


def is_valid_1(passport: str):
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    fields = passport.split()
    return (set(map(lambda x: x.split(':')[0], fields)) - {'cid'}) == required


def is_valid_2(passport: str):
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    rules = {
        'byr': lambda x: re.match("\d{4}$", x) and (1920 <= int(x) <= 2002),
        'iyr': lambda x: re.match("\d{4}$", x) and (2010 <= int(x) <= 2020),
        'eyr': lambda x: re.match("\d{4}$", x) and (2020 <= int(x) <= 2030),
        'hgt': lambda x: re.match("\d+(cm|in)$", x)
        and ((not re.match("\d+cm$", x)) or (150 <= int(re.match("(\d+)cm", x).group(1)) <= 193))
        and ((not re.match("\d+in$", x)) or (59 <= int(re.match("(\d+)in", x).group(1)) <= 76)),
        'hcl': lambda x: re.match("#[a-f0-9]{6}$", x),
        'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': lambda x: re.match("\d{9}$", x)
    }
    fields = passport.split()
    return ((set(map(lambda x: x.split(':')[0], fields)) - {'cid'}) == required) \
        and all(map(lambda x: x.split(':')[0] == 'cid' or bool(rules[x.split(':')[0]](x.split(':')[1])), fields))


def load_passports():
    passwords = []
    lines = fileinput.input()
    password = ''
    for l in lines:
        if l == '\n':
            passwords.append(password)
            password = ''
        else:
            password += " " + l.rstrip()
    passwords.append(password)
    return map(lambda p: p.rstrip().lstrip(), passwords)


# print(sum(map(is_valid_1, load_passports())))
print(sum(map(is_valid_2, load_passports())))
