# LeetCode 0394 - Decode String
# https://leetcode.com/problems/decode-string/


class Solution:
    def decodeString(self, s: str) -> str:
        stack: list[tuple[str, int]] = []
        current = ""
        number = 0

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char == "[":
                stack.append((current, number))
                current = ""
                number = 0
            elif char == "]":
                previous, count = stack.pop()
                current = previous + current * count
            else:
                current += char

        return current
