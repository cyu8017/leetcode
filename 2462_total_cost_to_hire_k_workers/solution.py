# LeetCode 2462 - Total Cost to Hire K Workers
# https://leetcode.com/problems/total-cost-to-hire-k-workers/

import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left_h = []
        right_h = []
        l, r = 0, n - 1
        while l <= r and len(left_h) < candidates:
            heapq.heappush(left_h, (costs[l], l))
            l += 1
        while r >= l and len(right_h) < candidates:
            heapq.heappush(right_h, (costs[r], r))
            r -= 1
        ans = 0
        for _ in range(k):
            use_left = False
            if left_h and right_h:
                lt, rt = left_h[0], right_h[0]
                if lt[0] < rt[0] or (lt[0] == rt[0] and lt[1] <= rt[1]):
                    use_left = True
            elif left_h:
                use_left = True
            if use_left:
                ans += heapq.heappop(left_h)[0]
                if l <= r:
                    heapq.heappush(left_h, (costs[l], l))
                    l += 1
            else:
                ans += heapq.heappop(right_h)[0]
                if l <= r:
                    heapq.heappush(right_h, (costs[r], r))
                    r -= 1
        return ans
