# LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stk = []
        ans = 0
        for x in nums:
            while stk and stk[-1] > x:
                ans += 1
                stk.pop()
            if x != 0 and (not stk or stk[-1] != x):
                stk.append(x)
        ans += len(stk)
        return ans
