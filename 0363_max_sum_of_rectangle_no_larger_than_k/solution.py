# LeetCode 0363 - Max Sum of Rectangle No Larger Than K
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        result = float("-inf")

        for top in range(rows):
            col_sums = [0] * cols
            for bottom in range(top, rows):
                prefix_sums = [0]
                running = 0
                for col in range(cols):
                    col_sums[col] += matrix[bottom][col]
                    running += col_sums[col]
                    index = bisect.bisect_left(prefix_sums, running - k)
                    if index < len(prefix_sums):
                        result = max(result, running - prefix_sums[index])
                    bisect.insort(prefix_sums, running)

        return result
