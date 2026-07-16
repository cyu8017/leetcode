# LeetCode 1074 - Number of Submatrices That Sum to Target
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        ans = 0
        for left in range(cols):
            row_sum = [0] * rows
            for right in range(left, cols):
                for r in range(rows):
                    row_sum[r] += matrix[r][right]
                prefix = 0
                seen: dict[int, int] = defaultdict(int)
                seen[0] = 1
                for val in row_sum:
                    prefix += val
                    ans += seen[prefix - target]
                    seen[prefix] += 1
        return ans
