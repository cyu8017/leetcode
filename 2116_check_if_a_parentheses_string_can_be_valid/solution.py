# LeetCode 2116 - Check if a Parentheses String Can Be Valid
# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        bal = 0
        for i in range(n):
            if locked[i] == "0" or s[i] == "(":
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        bal = 0
        for i in range(n - 1, (0) - 1, -1):
            if locked[i] == "0" or s[i] == ")":
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        return True
