# LeetCode 2330 - Valid Palindrome IV
# https://leetcode.com/problems/valid-palindrome-iv/

class Solution:
    def makePalindrome(self, s: str) -> bool:
        diff = 0
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                diff += 1
                if diff > 2:
                    return False
            i += 1
            j -= 1
        return True
