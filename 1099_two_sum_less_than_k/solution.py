# LeetCode 1099 - Two Sum Less Than K
# https://leetcode.com/problems/two-sum-less-than-k/

class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        nums.sort()
        lo, hi = 0, len(nums) - 1
        ans = -1
        while lo < hi:
            total = nums[lo] + nums[hi]
            if total < k:
                ans = max(ans, total)
                lo += 1
            else:
                hi -= 1
        return ans
