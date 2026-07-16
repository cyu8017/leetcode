# LeetCode 0032 - Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        best = 0

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    best = max(best, i - stack[-1])

        return best
