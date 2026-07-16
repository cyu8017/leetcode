# LeetCode 1349 - Maximum Students Taking Exam

from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        rows, cols = len(seats), len(seats[0])
        valid_rows = []
        for row in seats:
            available = sum((cell == ".") << c for c, cell in enumerate(row))
            valid_rows.append([mask for mask in range(1 << cols)
                               if mask & ~available == 0 and mask & (mask << 1) == 0])
        dp = {0: 0}
        for masks in valid_rows:
            nxt = {}
            for mask in masks:
                for previous, count in dp.items():
                    if mask & (previous << 1) == 0 and mask & (previous >> 1) == 0:
                        nxt[mask] = max(nxt.get(mask, 0), count + mask.bit_count())
            dp = nxt
        return max(dp.values())
