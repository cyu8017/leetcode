# LeetCode 0823 - Binary Trees With Factors
# https://leetcode.com/problems/binary-trees-with-factors/

class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        for i, x in enumerate(arr):
            ways = 1
            for j in range(i):
                left = arr[j]
                if x % left == 0:
                    right = x // left
                    if right in dp:
                        ways = (ways + dp[left] * dp[right]) % MOD
            dp[x] = ways
        return sum(dp.values()) % MOD
