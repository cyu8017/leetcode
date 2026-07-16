# LeetCode 0316 - Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {char: index for index, char in enumerate(s)}
        stack: list[str] = []
        seen: set[str] = set()
        for index, char in enumerate(s):
            if char in seen:
                continue
            while stack and stack[-1] > char and last_index[stack[-1]] > index:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return "".join(stack)
