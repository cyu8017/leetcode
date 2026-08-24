# LeetCode 3110 - Score of a String
# https://leetcode.com/problems/score-of-a-string/


class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            ans += abs(ord(s[i - 1]) - ord(s[i]))
        return ans
