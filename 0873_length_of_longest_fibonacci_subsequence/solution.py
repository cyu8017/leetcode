# LeetCode 0873 - Length of Longest Fibonacci Subsequence
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        dp = [[2] * n for _ in range(n)]
        ans = 0
        for j in range(n):
            for i in range(j):
                k = index.get(arr[j] - arr[i])
                if k is not None and k < i:
                    dp[i][j] = dp[k][i] + 1
                    ans = max(ans, dp[i][j])
        return ans if ans >= 3 else 0
