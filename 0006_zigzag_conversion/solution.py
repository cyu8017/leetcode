# LeetCode 0006 - Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        index = 0
        step = 1

        for ch in s:
            rows[index] += ch
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return "".join(rows)
