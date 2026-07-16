# LeetCode 1027 - Longest Arithmetic Subsequence
# https://leetcode.com/problems/longest-arithmetic-subsequence/

class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        dp: list[dict[int, int]] = [dict() for _ in nums]
        ans = 1
        for j in range(1, len(nums)):
            for i in range(j):
                d = nums[j] - nums[i]
                dp[j][d] = dp[i].get(d, 1) + 1
                ans = max(ans, dp[j][d])
        return ans
