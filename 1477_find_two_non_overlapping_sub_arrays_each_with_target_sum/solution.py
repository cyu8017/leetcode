from typing import List, Optional

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        inf, left, total, best, ans = 10**9, 0, 0, 10**9, 10**9
        shortest = [inf] * len(arr)
        for right, x in enumerate(arr):
            total += x
            while total > target:
                total -= arr[left]; left += 1
            if total == target:
                length = right - left + 1
                if left:
                    ans = min(ans, length + shortest[left-1])
                best = min(best, length)
            shortest[right] = best
        return -1 if ans == inf else ans
