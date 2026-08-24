# LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 1000000007
        sl = {}
        n = len(nums)
        f = [0] * (n + 1)
        g = [0] * (n + 1)
        f[0] = g[0] = 1
        keys = []

        def add(v: int) -> None:
            if v not in sl:
                sl[v] = 0
                lo, hi = 0, len(keys)
                while lo < hi:
                    mid = (lo + hi) >> 1
                    if keys[mid] < v:
                        lo = mid + 1
                    else:
                        hi = mid
                keys.insert(lo, v)
            sl[v] += 1

        def rem(v: int) -> None:
            c = sl[v] - 1
            if c == 0:
                del sl[v]
                ix = keys.index(v)
                if ix >= 0:
                    keys.pop(ix)
            else:
                sl[v] = c

        l = 1
        for r in range(1, n + 1):
            add(nums[r - 1])
            while keys[-1] - keys[0] > k:
                rem(nums[l - 1])
                l += 1
            f[r] = g[r - 1]
            if l >= 2:
                f[r] = (f[r] - g[l - 2] + mod) % mod
            g[r] = (g[r - 1] + f[r]) % mod
        return f[n]
