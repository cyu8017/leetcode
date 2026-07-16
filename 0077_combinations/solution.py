# LeetCode 0077 - Combinations
# https://leetcode.com/problems/combinations/

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                result.append(path[:])
                return

            remaining = k - len(path)
            for i in range(start, n - remaining + 2):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return result
