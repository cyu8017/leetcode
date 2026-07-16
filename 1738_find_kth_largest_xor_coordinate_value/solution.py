from heapq import nlargest
from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        pref = [[0] * (cols + 1) for _ in range(rows + 1)]
        values = []
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                pref[r][c] = pref[r - 1][c] ^ pref[r][c - 1] ^ pref[r - 1][c - 1] ^ matrix[r - 1][c - 1]
                values.append(pref[r][c])
        return nlargest(k, values)[-1]
