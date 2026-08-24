# LeetCode 3312 - Sorted GCD Pair Queries
# https://leetcode.com/problems/sorted-gcd-pair-queries/

from typing import List


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_v = 0
        for x in nums:
            if x > max_v:
                max_v = x
        cnt = [0] * (max_v + 1)
        for x in nums:
            cnt[x] += 1
        div_cnt = [0] * (max_v + 1)
        for g in range(1, max_v + 1):
            c = 0
            for m in range(g, max_v + 1, g):
                c += cnt[m]
            div_cnt[g] = c * (c - 1) // 2
        exact = [0] * (max_v + 1)
        for g in range(max_v, 0, -1):
            exact[g] = div_cnt[g]
            for m in range(2 * g, max_v + 1, g):
                exact[g] -= exact[m]
        pref = [0] * (max_v + 1)
        for g in range(1, max_v + 1):
            pref[g] = pref[g - 1] + exact[g]
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            lo, hi = 1, max_v
            while lo < hi:
                mid = (lo + hi) >> 1
                if pref[mid] > q:
                    hi = mid
                else:
                    lo = mid + 1
            ans[i] = lo
        return ans
