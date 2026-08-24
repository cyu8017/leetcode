# LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        uniq = []
        for x in banned:
            if 1 <= x <= n and (not uniq or uniq[-1] != x):
                uniq.append(x)
        ans = 0
        remain = maxSum
        prev = 0

        def check(l: int, r: int) -> None:
            nonlocal ans, remain
            if l > r or remain <= 0:
                return
            lo, hi = l, r
            best = l - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                cnt = mid - l + 1
                s = (l + mid) * cnt // 2
                if s <= remain:
                    best = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            if best >= l:
                cnt = best - l + 1
                ans += cnt
                remain -= (l + best) * cnt // 2

        for b in uniq:
            check(prev + 1, b - 1)
            prev = b
        check(prev + 1, n)
        return ans
