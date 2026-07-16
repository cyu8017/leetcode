# LeetCode 0709 - To Lower Case
# https://leetcode.com/problems/to-lower-case/


class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join(
            chr(ord(ch) + 32) if "A" <= ch <= "Z" else ch for ch in s
        )
