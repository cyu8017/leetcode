# LeetCode 0254 - Factor Combinations
# https://leetcode.com/problems/factor-combinations/

from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result: list[list[int]] = []

        def backtrack(remain: int, path: list[int], start: int) -> None:
            if start > remain:
                if len(path) > 1:
                    result.append(path[:])
                return
            factor = start
            while factor * factor <= remain:
                if remain % factor == 0:
                    path.append(factor)
                    backtrack(remain // factor, path, factor)
                    path.pop()
                factor += 1
            if path:
                path.append(remain)
                if len(path) > 1:
                    result.append(path[:])
                path.pop()

        backtrack(n, [], 2)
        return result
