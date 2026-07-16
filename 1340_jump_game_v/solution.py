# LeetCode 1340 - Jump Game V

from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [1] * len(arr)
        for _, i in sorted((value, i) for i, value in enumerate(arr)):
            for step in (-1, 1):
                j = i + step
                while 0 <= j < len(arr) and abs(j - i) <= d and arr[j] < arr[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    j += step
        return max(dp)
