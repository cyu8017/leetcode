# LeetCode 1048 - Longest String Chain
# https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=len)
        dp: dict[str, int] = {}
        ans = 1
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                prev = w[:i] + w[i + 1 :]
                if prev in dp:
                    dp[w] = max(dp[w], dp[prev] + 1)
            ans = max(ans, dp[w])
        return ans
