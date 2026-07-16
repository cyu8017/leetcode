# LeetCode 0799 - Champagne Tower
# https://leetcode.com/problems/champagne-tower/


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [float(poured)]
        for r in range(query_row):
            next_row = [0.0] * (r + 2)
            for i, amount in enumerate(row):
                overflow = (amount - 1.0) / 2.0
                if overflow > 0:
                    next_row[i] += overflow
                    next_row[i + 1] += overflow
            row = next_row
        return min(1.0, row[query_glass])
