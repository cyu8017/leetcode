from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg = 0
        mn = float("inf")
        for row in matrix:
            for x in row:
                if x < 0:
                    neg += 1
                ax = abs(x)
                total += ax
                mn = min(mn, ax)
        if neg % 2 == 0:
            return total
        return total - 2 * mn
