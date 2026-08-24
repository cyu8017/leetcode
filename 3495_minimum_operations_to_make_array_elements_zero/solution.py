# LeetCode 3495 - Minimum Operations to Make Array Elements Zero
# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

from typing import List


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def ops_to_zero(x: int) -> int:
            ops = 0
            while x > 0:
                x //= 4
                ops += 1
            return ops

        ans = 0
        for q in queries:
            l, r = q[0], q[1]
            s = 0
            for x in range(l, r + 1):
                s += ops_to_zero(x)
            ans += (s + 1) // 2
        return ans
