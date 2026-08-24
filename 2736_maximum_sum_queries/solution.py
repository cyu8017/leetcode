# LeetCode 2736 - Maximum Sum Queries
# https://leetcode.com/problems/maximum-sum-queries/

from typing import List


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        pts = [(nums1[i], nums2[i], nums1[i] + nums2[i]) for i in range(n)]
        pts.sort(key=lambda p: -p[0])
        qs = [(q[0], q[1], i) for i, q in enumerate(queries)]
        qs.sort(key=lambda q: -q[0])
        ys = sorted(list(nums2) + [q[1] for q in queries])
        uniq = []
        for y in ys:
            if not uniq or uniq[-1] != y:
                uniq.append(y)
        m = len(uniq)
        bit = [-1] * (m + 2)

        def rank(y: int) -> int:
            lo, hi = 0, m
            while lo < hi:
                mid = (lo + hi) >> 1
                if uniq[mid] < y:
                    lo = mid + 1
                else:
                    hi = mid
            return lo + 1

        def update(i: int, v: int) -> None:
            while i <= m:
                bit[i] = max(bit[i], v)
                i += i & -i

        def query(i: int) -> int:
            best = -1
            while i > 0:
                best = max(best, bit[i])
                i -= i & -i
            return best

        ans = [0] * len(queries)
        j = 0
        for q in qs:
            while j < n and pts[j][0] >= q[0]:
                update(m - rank(pts[j][1]) + 1, pts[j][2])
                j += 1
            ans[q[2]] = query(m - rank(q[1]) + 1)
        return ans
