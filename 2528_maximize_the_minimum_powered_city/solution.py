# LeetCode 2528 - Maximize the Minimum Powered City
# https://leetcode.com/problems/maximize-the-minimum-powered-city/

from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        diff = [0] * (n + 1)
        for i in range(n):
            L = max(0, i - r)
            R = min(n - 1, i + r)
            diff[L] += stations[i]
            diff[R + 1] -= stations[i]
        power = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            power[i] = cur
        lo = 0
        hi = k
        for p in power:
            if p > hi:
                hi = p
        hi += k

        def ok(x: int) -> bool:
            extra = [0] * (n + 1)
            have = 0
            used = 0
            for i in range(n):
                have += extra[i]
                need = x - (power[i] + have)
                if need > 0:
                    used += need
                    if used > k:
                        return False
                    have += need
                    end = i + 2 * r
                    if end + 1 <= n:
                        extra[end + 1] -= need
            return True

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
