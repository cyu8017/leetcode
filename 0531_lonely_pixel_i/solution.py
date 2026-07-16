# LeetCode 0531 - Lonely Pixel I
# https://leetcode.com/problems/lonely-pixel-i/

from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = len(picture)
        cols = len(picture[0])
        row_counts = [row.count("B") for row in picture]
        col_counts = [
            sum(picture[r][c] == "B" for r in range(rows)) for c in range(cols)
        ]

        lonely = 0
        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == "B" and row_counts[r] == 1 and col_counts[c] == 1:
                    lonely += 1
        return lonely
