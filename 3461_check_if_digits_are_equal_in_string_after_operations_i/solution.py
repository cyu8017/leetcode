# LeetCode 3461 - Check If Digits Are Equal in String After Operations I
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        b = list(s)
        while len(b) > 2:
            nb = [""] * (len(b) - 1)
            for i in range(len(b) - 1):
                nb[i] = str((ord(b[i]) - 48 + ord(b[i + 1]) - 48) % 10)
            b = nb
        return b[0] == b[1]
