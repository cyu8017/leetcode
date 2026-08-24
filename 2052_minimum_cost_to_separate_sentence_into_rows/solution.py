# LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
# https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/


class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:
        words = sentence.strip().split()
        n = len(words)
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            length = -1
            for j in range(i, n):
                length += 1 + len(words[j])
                if length > k:
                    break
                cost = 0
                if j < n - 1:
                    extra = k - length
                    cost = extra * extra
                dp[i] = min(dp[i], cost + dp[j + 1])
        return dp[0]
