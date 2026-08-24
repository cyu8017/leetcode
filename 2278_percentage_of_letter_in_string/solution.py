# LeetCode 2278 - Percentage of Letter in String
# https://leetcode.com/problems/percentage-of-letter-in-string/


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = 0
        for c in s:
            if c == letter:
                cnt += 1
        return cnt * 100 // len(s)
