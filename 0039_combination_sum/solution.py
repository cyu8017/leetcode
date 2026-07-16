# LeetCode 0039 - Combination Sum
# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(start: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result
