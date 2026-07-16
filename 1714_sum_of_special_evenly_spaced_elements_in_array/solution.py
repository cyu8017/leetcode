from math import isqrt
from typing import List


class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        n = len(nums)
        block = isqrt(n) + 1
        dp = [[0] * n for _ in range(block)]
        for step in range(1, block):
            for i in range(n - 1, -1, -1):
                dp[step][i] = (nums[i] + (dp[step][i + step] if i + step < n else 0)) % mod
        ans = []
        for start, step in queries:
            if step < block:
                ans.append(dp[step][start])
            else:
                total = 0
                for i in range(start, n, step):
                    total += nums[i]
                ans.append(total % mod)
        return ans
