# LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
# https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

from typing import List
class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        MOD = 1000000007
        masks = []
        def gen(remain, mask):
            if remain == 0:
                masks.append(mask)
                return
            for b in bricks:
                if b <= remain:
                    nm = mask
                    if remain - b > 0:
                        nm |= 1 << (remain - b)
                    gen(remain - b, nm)

        gen(width, 0)
        m = len(masks)
        compat = [[] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                if (masks[i] & masks[j]) == 0:
                    compat[i].append(j)
        dp = [1] * (m)
        for h in range(1, height):
            ndp = [0] * (m)
            for i in range(m):
                for j in compat[i]:
                    ndp[j] = (ndp[j] + dp[i]) % MOD
            dp = ndp
        ans = 0
        for v in dp:
            ans = (ans + v) % MOD
        return ans
