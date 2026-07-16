# LeetCode 0020 - Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif not stack or stack.pop() != pairs[ch]:
                return False

        return not stack
