# LeetCode 0795 - Number of Subarrays with Bounded Maximum
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_at_most(bound: int) -> int:
            ans = cur = 0
            for num in nums:
                if num <= bound:
                    cur += 1
                    ans += cur
                else:
                    cur = 0
            return ans

        return count_at_most(right) - count_at_most(left - 1)
