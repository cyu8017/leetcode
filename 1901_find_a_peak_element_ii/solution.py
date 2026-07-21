from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        lo, hi = 0, cols - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            max_row = max(range(rows), key=lambda r: mat[r][mid])
            left = mat[max_row][mid - 1] if mid else -1
            right = mat[max_row][mid + 1] if mid + 1 < cols else -1
            if mat[max_row][mid] >= left and mat[max_row][mid] >= right:
                return [max_row, mid]
            if left > mat[max_row][mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return [0, 0]
