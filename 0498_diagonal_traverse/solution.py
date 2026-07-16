# LeetCode 0498 - Diagonal Traverse
# https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []
        rows, cols = len(mat), len(mat[0])
        result: list[int] = []
        row = col = 0
        upward = True

        for _ in range(rows * cols):
            result.append(mat[row][col])
            if upward:
                if col == cols - 1:
                    row += 1
                    upward = False
                elif row == 0:
                    col += 1
                    upward = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == rows - 1:
                    col += 1
                    upward = True
                elif col == 0:
                    row += 1
                    upward = True
                else:
                    row += 1
                    col -= 1
        return result
