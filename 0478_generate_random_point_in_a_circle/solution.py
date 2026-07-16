# LeetCode 0478 - Generate Random Point in a Circle
# https://leetcode.com/problems/generate-random-point-in-a-circle/

import random


def set_uniform(uniform_fn) -> None:
    global uniform
    uniform = uniform_fn


uniform = random.uniform


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> list[float]:
        while True:
            x = uniform(-self.radius, self.radius)
            y = uniform(-self.radius, self.radius)
            if x * x + y * y <= self.radius * self.radius:
                return [round(self.x_center + x, 5), round(self.y_center + y, 5)]
