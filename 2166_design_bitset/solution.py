# LeetCode 2166 - Design Bitset
# https://leetcode.com/problems/design-bitset/
class Bitset:
    def __init__(self, size):
        self.size = size
        self.bits = [0] * (size)
        self.ones = 0
        self.flipped = False

    def fix(self, idx):
        target = 0 if self.flipped else 1
        if self.bits[idx] != target:
            self.bits[idx] = target
            self.ones += 1

    def unfix(self, idx):
        target = 1 if self.flipped else 0
        if self.bits[idx] != target:
            self.bits[idx] = target
            self.ones -= 1

    def flip(self):
        self.flipped = not self.flipped
        self.ones = self.size - self.ones

    def all(self):
        return self.ones == self.size

    def one(self):
        return self.ones > 0

    def count(self):
        return self.ones

    def toString(self):
        b = [None] * (self.size)
        for i in range(self.size):
            v = self.bits[i]
            if self.flipped:
                v ^= 1
            b[i] = str(v)
        return "".join(b)
