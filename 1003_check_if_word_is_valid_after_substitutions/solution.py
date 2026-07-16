# LeetCode 1003 - Check If Word Is Valid After Substitutions
# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 3 and stack[-3:] == ["a", "b", "c"]:
                stack[-3:] = []
        return not stack
