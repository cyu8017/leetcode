# LeetCode 0040 - Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: List[List[int]] = []

        def backtrack(start: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result
