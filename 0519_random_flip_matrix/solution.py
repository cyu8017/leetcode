# LeetCode 0519 - Random Flip Matrix
# https://leetcode.com/problems/random-flip-matrix/

import random


def set_uniform(uniform_fn) -> None:
    global uniform
    uniform = uniform_fn


uniform = random.uniform


class Solution:
    def __init__(self, m: int, n: int):
        self.rows = m
        self.cols = n
        self.total = m * n
        self.reset()

    def flip(self) -> list[int]:
        index = int(uniform(0, len(self.available) - 1))
        if index >= len(self.available):
            index = len(self.available) - 1
        value = self.available[index]
        self.available[index] = self.available[-1]
        self.available.pop()
        return [value // self.cols, value % self.cols]

    def reset(self) -> None:
        self.available = list(range(self.total))
