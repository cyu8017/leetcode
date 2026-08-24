# LeetCode 2351 - First Letter to Appear Twice
# https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = [False] * 26
        for c in s:
            i = ord(c) - 97
            if seen[i]:
                return c
            seen[i] = True
        return chr(0)
