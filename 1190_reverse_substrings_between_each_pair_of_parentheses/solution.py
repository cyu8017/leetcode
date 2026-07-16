# LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack: list[str] = []
        for ch in s:
            if ch == ")":
                chunk: list[str] = []
                while stack and stack[-1] != "(":
                    chunk.append(stack.pop())
                stack.pop()
                stack.extend(chunk)
            else:
                stack.append(ch)
        return "".join(stack)
