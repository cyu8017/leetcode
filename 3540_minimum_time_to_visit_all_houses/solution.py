# LeetCode 3540 - Minimum Time to Visit All Houses
# https://leetcode.com/problems/minimum-time-to-visit-all-houses/

from typing import List


class Solution:
    def minTotalTime(
        self, forward: List[int], backward: List[int], queries: List[int]
    ) -> int:
        n = len(forward)
        sum_b = sum(backward)
        pf = [0] * (n + 1)
        pb = [0] * (n + 1)
        for i in range(n):
            pf[i + 1] = pf[i] + forward[i]
            pb[i + 1] = pb[i] + backward[i]
        ans = 0
        pos = 0
        for q in queries:
            r = 0
            if q < pos:
                r = pf[n]
            r += pf[q] - pf[pos]
            lft = 0
            if q > pos:
                lft = sum_b
            lft += pb[pos] - pb[q]
            ans += min(lft, r)
            pos = q
        return ans
