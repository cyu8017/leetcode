from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                prefix[r+1][c+1] = mat[r][c] + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c]
        def possible(size):
            return any(prefix[r][c] - prefix[r-size][c] - prefix[r][c-size] + prefix[r-size][c-size] <= threshold
                       for r in range(size, m + 1) for c in range(size, n + 1))
        lo, hi = 0, min(m, n)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if possible(mid): lo = mid
            else: hi = mid - 1
        return lo
