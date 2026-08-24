# LeetCode 2070 - Most Beautiful Item for Each Query
# https://leetcode.com/problems/most-beautiful-item-for-each-query/

from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda it: it[0])
        max_b = 0
        for it in items:
            max_b = max(max_b, it[1])
            it[1] = max_b
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            lo, hi = 0, len(items)
            while lo < hi:
                mid = (lo + hi) >> 1
                if items[mid][0] <= q:
                    lo = mid + 1
                else:
                    hi = mid
            ans[i] = 0 if lo == 0 else items[lo - 1][1]
        return ans
