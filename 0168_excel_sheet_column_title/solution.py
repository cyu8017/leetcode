# LeetCode 0168 - Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars: list[str] = []
        while columnNumber:
            columnNumber -= 1
            chars.append(chr(ord("A") + columnNumber % 26))
            columnNumber //= 26
        return "".join(reversed(chars))
