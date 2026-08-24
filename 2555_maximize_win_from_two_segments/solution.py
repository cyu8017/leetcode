# LeetCode 2555 - Maximize Win From Two Segments
# https://leetcode.com/problems/maximize-win-from-two-segments/

from typing import List


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        dp = [0] * (n + 1)
        ans = 0
        left = 0
        for right in range(n):
            while prizePositions[right] - prizePositions[left] > k:
                left += 1
            cur = right - left + 1
            if dp[left] + cur > ans:
                ans = dp[left] + cur
            best = cur
            if dp[right] > best:
                best = dp[right]
            dp[right + 1] = best
        return ans
