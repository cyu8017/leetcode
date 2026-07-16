from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for value in (arr[n // 4], arr[n // 2], arr[3 * n // 4]):
            if arr.count(value) > n // 4:
                return value
        return arr[0]
