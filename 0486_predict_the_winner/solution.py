# LeetCode 0486 - Predict the Winner
# https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                dp[left][right] = max(
                    nums[left] - dp[left + 1][right],
                    nums[right] - dp[left][right - 1],
                )
        return dp[0][n - 1] >= 0
