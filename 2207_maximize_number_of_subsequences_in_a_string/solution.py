# LeetCode 2207 - Maximize Number of Subsequences in a String
# https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        a = pattern[0]
        b = pattern[1]
        def count(s):
            ca = 0
            ans = 0
            for ch in s:
                if ch == b:
                    ans += ca
                if ch == a:
                    ca += 1
            return ans

        return max(count(a + text), count(text + b))
