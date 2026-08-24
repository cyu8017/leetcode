# LeetCode 2563 - Count the Number of Fair Pairs
# https://leetcode.com/problems/count-the-number-of-fair-pairs/

from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def count(x: int) -> int:
            ans = 0
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] <= x:
                    ans += r - l
                    l += 1
                else:
                    r -= 1
            return ans

        return count(upper) - count(lower - 1)
