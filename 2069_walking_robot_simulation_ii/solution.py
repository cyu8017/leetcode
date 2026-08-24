# LeetCode 2069 - Walking Robot Simulation II
# https://leetcode.com/problems/walking-robot-simulation-ii/

from typing import List


class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.peri = 2 * (width + height) - 4
        self.pos = 0
        self.moved = False

    def getPosDir(self):
        p = self.pos
        if p == 0:
            if not self.moved:
                return [0, 0, 0]
            return [0, 0, 3]
        if p <= self.w - 1:
            return [p, 0, 0]
        p -= self.w - 1
        if p <= self.h - 1:
            return [self.w - 1, p, 1]
        p -= self.h - 1
        if p <= self.w - 1:
            return [self.w - 1 - p, self.h - 1, 2]
        p -= self.w - 1
        return [0, self.h - 1 - p, 3]

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.peri

    def getPos(self) -> List[int]:
        pd = self.getPosDir()
        return [pd[0], pd[1]]

    def getDir(self) -> str:
        names = ["East", "North", "West", "South"]
        return names[self.getPosDir()[2]]
