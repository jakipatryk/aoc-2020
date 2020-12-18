import fileinput
from functools import reduce


class NewMathUnit():
    def __init__(self, a):
        self.a = a

    def __mul__(self, other):
        return NewMathUnit(self.a * other.a)

    def __truediv__(self, other):
        return NewMathUnit(self.a + other.a)

    def __sub__(self, other):
        return NewMathUnit(self.a * other.a)


lines = list(map(lambda x: "".join(list(map(
    lambda c: f"NewMathUnit({c})" if c.isdigit() else c, x.rstrip()))), fileinput.input()))

# part 1
print(reduce(lambda acc, curr: acc + eval(curr).a,
             map(lambda e: e.replace("+", "/"), lines), 0))

# part 2
print(reduce(lambda acc, curr: acc + eval(curr).a,
             map(lambda e: e.replace("*", "-").replace("+", "/"), lines), 0))
