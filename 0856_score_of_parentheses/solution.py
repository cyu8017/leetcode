# LeetCode 0856 - Score of Parentheses
# https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max(2 * val, 1)
        return stack[0]
