# LeetCode 3532 - Path Existence Queries in a Graph I
# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        g = [0] * n
        cnt = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                cnt += 1
            g[i] = cnt
        return [g[q[0]] == g[q[1]] for q in queries]
