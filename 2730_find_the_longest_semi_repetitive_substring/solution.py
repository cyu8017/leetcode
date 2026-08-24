# LeetCode 2730 - Find the Longest Semi-Repetitive Substring
# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans, left, last_pair = 0, 0, -1
        for right in range(len(s)):
            if right > 0 and s[right] == s[right - 1]:
                if last_pair >= left:
                    left = last_pair + 1
                last_pair = right - 1
            ans = max(ans, right - left + 1)
        return ans
