# LeetCode 0682 - Baseball Game
# https://leetcode.com/problems/baseball-game/

from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack: list[int] = []
        for op in ops:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)
