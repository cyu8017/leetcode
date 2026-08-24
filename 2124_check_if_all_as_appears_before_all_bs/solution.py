# LeetCode 2124 - Check if All A's Appears Before All B's
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
class Solution:
    def checkString(self, s: str) -> bool:
        seenB = False
        for i in range(len(s)):
            c = s[i]
            if c == "b":
                seenB = True
            elif seenB:
                return False
        return True
