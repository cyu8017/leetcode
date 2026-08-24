# LeetCode 2940 - Find Building Where Alice and Bob Can Meet
# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

from typing import List


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        qn = len(queries)
        ans = [-1] * qn
        buckets = [[] for _ in range(len(heights))]
        for qi in range(qn):
            a, b = queries[qi][0], queries[qi][1]
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans[qi] = b
                continue
            buckets[b].append((heights[a], qi))
        st = []
        for i in range(len(heights) - 1, -1, -1):
            for h, qi in buckets[i]:
                lo, hi = 0, len(st) - 1
                pos = -1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if st[mid][0] > h:
                        pos = st[mid][1]
                        lo = mid + 1
                    else:
                        hi = mid - 1
                ans[qi] = pos
            while st and st[-1][0] <= heights[i]:
                st.pop()
            st.append((heights[i], i))
        return ans
