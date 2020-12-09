import re
import fileinput

lines = list(map(lambda x: x.rstrip(), fileinput.input()))


class GameConsole():
    def __init__(self, boot_code):
        self.accumulator = 0
        self.boot_code = boot_code

    def process(self):
        """
        returns (accumulator, has_loop)
        """
        actions = {
            'jmp': lambda arg, i, acc: (i + arg, acc),
            'nop': lambda arg, i, acc: (i + 1, acc),
            'acc': lambda arg, i, acc: (i + 1, acc + arg)
        }
        visited = [False] * len(self.boot_code)
        i = 0
        while i < len(self.boot_code):
            if visited[i]:
                return (self.accumulator, True)
            line = self.boot_code[i]
            visited[i] = True
            pattern = "(jmp|acc|nop) ([+\-]\d+)"
            match = re.match(pattern, line)
            action = match.group(1)
            arg = int(match.group(2))
            i, self.accumulator = actions[action](arg, i, self.accumulator)
        return (self.accumulator, False)

    def fix_loop(self):
        jumps = [i for i in range(len(self.boot_code))
                 if self.boot_code[i][0:3] == 'jmp']
        nops = [i for i in range(len(self.boot_code))
                if self.boot_code[i][0:3] == 'nop']
        for i in jumps:
            self.accumulator = 0
            self.boot_code[i] = 'nop' + self.boot_code[i][3:]
            acc, has_loop = self.process()
            if not has_loop:
                return acc
            self.boot_code[i] = 'jmp' + self.boot_code[i][3:]
        for i in nops:
            self.accumulator = 0
            self.boot_code[i] = 'jmp' + self.boot_code[i][3:]
            acc, has_loop = self.process()
            if not has_loop:
                return acc
            self.boot_code[i] = 'nop' + self.boot_code[i][3:]


game_console = GameConsole(lines)

# part 1
# print(game_console.process()[0])

# part 2
print(game_console.fix_loop())
