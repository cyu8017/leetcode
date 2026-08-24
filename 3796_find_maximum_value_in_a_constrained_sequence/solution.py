# LeetCode 3796 - Find Maximum Value in a Constrained Sequence
# https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

from typing import List


class Solution:
    def maxValue(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        INF = 2147483647 // 4
        bound = [INF] * n
        bound[0] = 0
        for r in restrictions:
            bound[r[0]] = r[1]
        for i in range(1, n):
            bound[i] = min(bound[i], bound[i - 1] + diff[i - 1])
        for i in range(n - 2, -1, -1):
            bound[i] = min(bound[i], bound[i + 1] + diff[i])
        ans = bound[0]
        for i in range(1, n):
            ans = max(ans, bound[i])
        return ans
