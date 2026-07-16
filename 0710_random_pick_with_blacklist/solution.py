# LeetCode 0710 - Random Pick with Blacklist
# https://leetcode.com/problems/random-pick-with-blacklist/

import random
from typing import List


def set_uniform(uniform_fn) -> None:
    global uniform
    uniform = uniform_fn


uniform = random.uniform


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.size = n - len(blacklist)
        black = set(blacklist)
        whites = (x for x in range(self.size, n) if x not in black)
        self.mapping = {b: next(whites) for b in blacklist if b < self.size}

    def pick(self) -> int:
        index = int(uniform(0, self.size))
        if index >= self.size:
            index = self.size - 1
        return self.mapping.get(index, index)
