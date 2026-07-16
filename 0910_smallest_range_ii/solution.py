# LeetCode 0910 - Smallest Range II
# https://leetcode.com/problems/smallest-range-ii/

class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            lo = min(nums[0] + k, nums[i + 1] - k)
            hi = max(nums[-1] - k, nums[i] + k)
            ans = min(ans, hi - lo)
        return ans
