class Solution:
    def maximumScore(self, nums, multipliers):
        from functools import lru_cache
        n, m = len(nums), len(multipliers)
        @lru_cache(None)
        def dp(i, left):
            if i == m:
                return 0
            right = n - 1 - (i - left)
            take_left = nums[left] * multipliers[i] + dp(i + 1, left + 1)
            take_right = nums[right] * multipliers[i] + dp(i + 1, left)
            return max(take_left, take_right)
        return dp(0, 0)
