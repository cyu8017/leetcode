# LeetCode 0302 - Smallest Rectangle Enclosing Black Pixels
# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

from typing import List


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        rows = len(image)
        cols = len(image[0])

        def column_has_black(col: int) -> bool:
            return any(image[row][col] == "1" for row in range(rows))

        def row_has_black(row: int) -> bool:
            return any(image[row][col] == "1" for col in range(cols))

        left, right = 0, y
        while left < right:
            mid = (left + right) // 2
            if column_has_black(mid):
                right = mid
            else:
                left = mid + 1
        left_bound = left

        left, right = y, cols - 1
        while left < right:
            mid = (left + right + 1) // 2
            if column_has_black(mid):
                left = mid
            else:
                right = mid - 1
        right_bound = left

        top, bottom = 0, x
        while top < bottom:
            mid = (top + bottom) // 2
            if row_has_black(mid):
                bottom = mid
            else:
                top = mid + 1
        top_bound = top

        top, bottom = x, rows - 1
        while top < bottom:
            mid = (top + bottom + 1) // 2
            if row_has_black(mid):
                top = mid
            else:
                bottom = mid - 1
        bottom_bound = top

        return (right_bound - left_bound + 1) * (bottom_bound - top_bound + 1)
