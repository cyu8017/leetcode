# LeetCode 3092 - Most Frequent IDs
# https://leetcode.com/problems/most-frequent-ids/

import heapq
from typing import List


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        n = len(nums)
        cnt = {}
        lazy = {}
        ans = [0] * n
        pq = []
        for i in range(n):
            x, f = nums[i], freq[i]
            old = cnt.get(x, 0)
            lazy[old] = lazy.get(old, 0) + 1
            neu = old + f
            cnt[x] = neu
            heapq.heappush(pq, -neu)
            while pq and lazy.get(-pq[0], 0) > 0:
                top = -heapq.heappop(pq)
                lazy[top] -= 1
            ans[i] = -pq[0] if pq else 0
        return ans
