# LeetCode 3707 - Equal Score Substrings
# https://leetcode.com/problems/equal-score-substrings/


class Solution:
    def scoreBalance(self, s: str) -> bool:
        l = 0
        r = 0
        for c in s:
            r += (ord(c) - 97) + 1
        for i in range(len(s) - 1):
            x = (ord(s[i]) - 97) + 1
            l += x
            r -= x
            if l == r:
                return True
        return False
