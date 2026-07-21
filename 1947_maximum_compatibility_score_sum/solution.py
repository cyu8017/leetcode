from typing import List
from functools import lru_cache

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        score = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                score[i][j] = sum(a == b for a, b in zip(students[i], mentors[j]))

        @lru_cache(None)
        def dp(i: int, mask: int) -> int:
            if i == m:
                return 0
            best = 0
            for j in range(m):
                if mask & (1 << j) == 0:
                    best = max(best, score[i][j] + dp(i + 1, mask | (1 << j)))
            return best

        return dp(0, 0)
