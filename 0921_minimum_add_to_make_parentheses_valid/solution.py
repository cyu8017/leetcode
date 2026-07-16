# LeetCode 0921 - Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_need = close_need = 0
        for ch in s:
            if ch == "(":
                close_need += 1
            elif close_need:
                close_need -= 1
            else:
                open_need += 1
        return open_need + close_need
