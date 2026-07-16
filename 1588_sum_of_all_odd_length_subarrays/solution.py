from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        return sum(x * (((i + 1) * (n - i) + 1) // 2) for i, x in enumerate(arr))
