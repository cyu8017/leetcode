# LeetCode 3717 - Minimum Operations to Make the Array Beautiful
# https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

from typing import List
import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        f = {nums[0]: 0}
        for i in range(1, len(nums)):
            x = nums[i]
            g = {}
            for pre, s in f.items():
                cur = math.ceil(x / pre) * pre
                while cur <= 100:
                    val = s + (cur - x)
                    old = g.get(cur)
                    if old is None or old > val:
                        g[cur] = val
                    cur += pre
            f = g
        return min(f.values()) if f else 0
