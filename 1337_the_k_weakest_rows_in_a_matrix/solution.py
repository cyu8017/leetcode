# LeetCode 1337 - The K Weakest Rows In A Matrix

from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted(range(len(mat)), key=lambda i: (sum(mat[i]), i))[:k]
