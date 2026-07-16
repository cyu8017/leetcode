# LeetCode 0891 - Sum of Subsequence Widths
# https://leetcode.com/problems/sum-of-subsequence-widths/

class Solution:
    def sumSubseqWidths(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD
        ans = 0
        for i, x in enumerate(nums):
            ans = (ans + x * (pow2[i] - pow2[n - 1 - i])) % MOD
        return ans
