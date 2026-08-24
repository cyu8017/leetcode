# LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        has1s = False
        has1t = False
        for i in range(len(s)):
            if s[i] == "1":
                has1s = True
            if target[i] == "1":
                has1t = True
        return has1s == has1t
