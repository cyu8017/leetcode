# LeetCode 0497 - Random Point in Non-overlapping Rectangles
# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

import random


def set_uniform(uniform_fn) -> None:
    global uniform
    uniform = uniform_fn


uniform = random.uniform


class Solution:
    def __init__(self, rects: list[list[int]]):
        self.rects = rects
        self.prefix: list[int] = []
        total = 0
        for a, b, x, y in rects:
            total += (x - a + 1) * (y - b + 1)
            self.prefix.append(total)
        self.total = total

    def pick(self) -> list[int]:
        index = int(uniform(0, self.total))
        if index >= self.total:
            index = self.total - 1
        for a, b, x, y in self.rects:
            width = x - a + 1
            height = y - b + 1
            size = width * height
            if index < size:
                offset_x = index % width
                offset_y = index // width
                return [a + offset_x, b + offset_y]
            index -= size
        return [self.rects[-1][0], self.rects[-1][1]]
