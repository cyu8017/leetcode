# LeetCode 1314 - Matrix Block Sum

from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
        answer = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                r1, c1, r2, c2 = max(0, r-k), max(0, c-k), min(m, r+k+1), min(n, c+k+1)
                answer[r][c] = prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]
        return answer
