# LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

from typing import List, Optional

_FACTORS3629: Optional[List[List[int]]] = None


def factors3629() -> List[List[int]]:
    global _FACTORS3629
    if _FACTORS3629 is None:
        mx = 1000001
        factors = [[] for _ in range(mx)]
        for i in range(2, mx):
            if not factors[i]:
                for j in range(i, mx, i):
                    factors[j].append(i)
        _FACTORS3629 = factors
    return _FACTORS3629


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        fac = factors3629()
        n = len(nums)
        g = {}
        for i, v in enumerate(nums):
            for p in fac[v]:
                g.setdefault(p, []).append(i)
        ans = 0
        vis = [False] * n
        vis[0] = True
        q = [0]
        while True:
            nq = []
            for i in q:
                if i == n - 1:
                    return ans
                idx = list(g.get(nums[i], []))
                idx.append(i + 1)
                if i > 0:
                    idx.append(i - 1)
                for j in idx:
                    if 0 <= j < n and not vis[j]:
                        vis[j] = True
                        nq.append(j)
                g[nums[i]] = []
            q = nq
            ans += 1
