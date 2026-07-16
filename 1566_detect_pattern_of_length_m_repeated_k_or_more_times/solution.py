from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        run = 0
        for i in range(m, len(arr)):
            run = run + 1 if arr[i] == arr[i - m] else 0
            if run >= m * (k - 1):
                return True
        return False
