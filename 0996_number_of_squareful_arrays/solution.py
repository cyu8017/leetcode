# LeetCode 0996 - Number of Squareful Arrays
# https://leetcode.com/problems/number-of-squareful-arrays/

from collections import Counter
from math import isqrt


class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        count = Counter(nums)
        graph = {x: [] for x in count}
        for a in count:
            for b in count:
                s = a + b
                r = isqrt(s)
                if r * r == s:
                    graph[a].append(b)
        self.ans = 0

        def dfs(x: int, remain: int) -> None:
            if remain == 0:
                self.ans += 1
                return
            for y in graph[x]:
                if count[y]:
                    count[y] -= 1
                    dfs(y, remain - 1)
                    count[y] += 1

        for x in count:
            count[x] -= 1
            dfs(x, len(nums) - 1)
            count[x] += 1
        return self.ans
