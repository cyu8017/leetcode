# LeetCode 1180 - Count Substrings with Only One Distinct Letter
# https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

class Solution:
    def countLetters(self, s: str) -> int:
        ans = length = 1
        for i in range(1, len(s)):
            length = length + 1 if s[i] == s[i - 1] else 1
            ans += length
        return ans
