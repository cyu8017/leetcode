# LeetCode 0386 - Lexicographical Numbers
# https://leetcode.com/problems/lexicographical-numbers/

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result: list[int] = []

        def dfs(current: int) -> None:
            if current > n:
                return
            result.append(current)
            dfs(current * 10)
            if current % 10 < 9:
                dfs(current + 1)

        dfs(1)
        return result
