from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        prefix = []
        total = 0
        for value in nums:
            total += value
            prefix.append(total)
        ans = 0
        n = len(nums)
        for i in range(n - 2):
            left = prefix[i]
            lo = bisect_left(prefix, 2 * left, i + 1, n - 1)
            hi = bisect_right(prefix, (total + left) // 2, lo, n - 1)
            ans = (ans + hi - lo) % mod
        return ans
