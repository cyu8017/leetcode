# LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        lst = nums[:]
        ops = 0
        while True:
            seen = set()
            dup = False
            for x in lst:
                if x in seen:
                    dup = True
                    break
                seen.add(x)
            if not dup:
                return ops
            if len(lst) <= 3:
                return ops + 1
            lst = lst[3:]
            ops += 1
