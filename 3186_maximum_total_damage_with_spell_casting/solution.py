# LeetCode 3186 - Maximum Total Damage With Spell Casting
# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        n = len(power)
        power.sort()
        cnt = {}
        nxt = [0] * n
        f = [0] * n

        def lower_bound(a: List[int], x: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        for i in range(n):
            cnt[power[i]] = cnt.get(power[i], 0) + 1
            nxt[i] = lower_bound(power, power[i] + 3)

        def dfs(i: int) -> int:
            if i >= n:
                return 0
            if f[i] != 0:
                return f[i]
            a = dfs(i + cnt[power[i]])
            b = power[i] * cnt[power[i]] + dfs(nxt[i])
            f[i] = max(a, b)
            return f[i]

        return dfs(0)
