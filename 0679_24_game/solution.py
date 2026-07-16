# LeetCode 0679 - 24 Game
# https://leetcode.com/problems/24-game/

from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        eps = 1e-6

        def dfs(nums: list[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < eps
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    candidates = [a + b, a - b, a * b]
                    if abs(b) > eps:
                        candidates.append(a / b)
                    for value in candidates:
                        if dfs(rest + [value]):
                            return True
            return False

        return dfs([float(x) for x in cards])
