# LeetCode 1072 - Flip Columns For Maximum Number of Equal Rows
# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        patterns = Counter()
        for row in matrix:
            base = row[0]
            key = tuple(x ^ base for x in row)
            patterns[key] += 1
        return max(patterns.values())
