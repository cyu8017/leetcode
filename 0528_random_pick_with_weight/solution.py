# LeetCode 0528 - Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/

import bisect
import random


def set_uniform(uniform_fn) -> None:
    global uniform
    uniform = uniform_fn


uniform = random.uniform


class Solution:
    def __init__(self, w: list[int]):
        self.prefix: list[int] = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = int(uniform(0, self.total))
        if target >= self.total:
            target = self.total - 1
        return bisect.bisect_right(self.prefix, target)
