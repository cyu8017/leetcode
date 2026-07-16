from typing import List, Optional

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod, left, right, ans = 1_000_000_007, 0, len(nums)-1, 0
        powers = [1] * (len(nums)+1)
        for i in range(1, len(powers)):
            powers[i] = powers[i-1] * 2 % mod
        while left <= right:
            if nums[left] + nums[right] <= target:
                ans = (ans + powers[right-left]) % mod
                left += 1
            else:
                right -= 1
        return ans
