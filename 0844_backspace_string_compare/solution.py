# LeetCode 0844 - Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(text: str) -> list[str]:
            stack: list[str] = []
            for ch in text:
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return stack

        return build(s) == build(t)
