from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows, cols = [0] * m, [0] * n
        for r, c in indices:
            rows[r] ^= 1
            cols[c] ^= 1
        return sum(rows[r] ^ cols[c] for r in range(m) for c in range(n))
