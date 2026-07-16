# LeetCode 0378 - Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:
            mid = (left + right) // 2
            count = 0
            column = rows - 1

            for row in range(rows):
                while column >= 0 and matrix[row][column] > mid:
                    column -= 1
                count += column + 1

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left
