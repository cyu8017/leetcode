# LeetCode 3366 - Minimum Array Sum
# https://leetcode.com/problems/minimum-array-sum/

from typing import List


def tryCand(ndp: List[List[float]], base: float, na: int, nb: int, v: int) -> None:
    if base + v < ndp[na][nb]:
        ndp[na][nb] = base + v


class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        inf = 1e18
        dp = [[inf] * (op2 + 1) for _ in range(op1 + 1)]
        dp[0][0] = 0
        for x in nums:
            ndp = [[inf] * (op2 + 1) for _ in range(op1 + 1)]
            for a in range(op1 + 1):
                for b in range(op2 + 1):
                    if dp[a][b] == inf:
                        continue
                    tryCand(ndp, dp[a][b], a, b, x)
                    if a < op1:
                        tryCand(ndp, dp[a][b], a + 1, b, (x + 1) // 2)
                    if b < op2 and x >= k:
                        tryCand(ndp, dp[a][b], a, b + 1, x - k)
                    if a < op1 and b < op2:
                        v1 = (x + 1) // 2
                        if v1 >= k:
                            tryCand(ndp, dp[a][b], a + 1, b + 1, v1 - k)
                        if x >= k:
                            tryCand(ndp, dp[a][b], a + 1, b + 1, (x - k + 1) // 2)
            dp = ndp
        ans = inf
        for a in range(op1 + 1):
            for b in range(op2 + 1):
                if dp[a][b] < ans:
                    ans = dp[a][b]
        return int(ans)
