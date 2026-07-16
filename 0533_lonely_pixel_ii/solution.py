# LeetCode 0533 - Lonely Pixel II
# https://leetcode.com/problems/lonely-pixel-ii/

from typing import List


class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        rows = len(picture)
        cols = len(picture[0])
        row_strings = ["".join(row) for row in picture]
        row_counts = [row.count("B") for row in picture]
        col_counts = [
            sum(picture[r][c] == "B" for r in range(rows)) for c in range(cols)
        ]

        lonely = 0
        for r in range(rows):
            if row_counts[r] != target:
                continue
            for c in range(cols):
                if picture[r][c] != "B" or col_counts[c] != target:
                    continue
                if all(
                    row_strings[r] == row_strings[i]
                    for i in range(rows)
                    if picture[i][c] == "B"
                ):
                    lonely += 1
        return lonely
