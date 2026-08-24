# LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

from typing import List


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        leftMost = [0] * n
        z = o = L = 0
        for R in range(n):
            if s[R] == "0":
                z += 1
            else:
                o += 1
            while z > k and o > k:
                if s[L] == "0":
                    z -= 1
                else:
                    o -= 1
                L += 1
            leftMost[R] = L
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (i - leftMost[i] + 1)
        ans = [0] * len(queries)
        for qi in range(len(queries)):
            l, r = queries[qi][0], queries[qi][1]
            lo, hi = l, r + 1
            while lo < hi:
                mid = (lo + hi) >> 1
                if leftMost[mid] < l:
                    lo = mid + 1
                else:
                    hi = mid
            res = 0
            if lo > l:
                m = lo - l
                res += m * (m + 1) // 2
            if lo <= r:
                res += pref[r + 1] - pref[lo]
            ans[qi] = res
        return ans
