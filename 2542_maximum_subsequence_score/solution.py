# LeetCode 2542 - Maximum Subsequence Score
# https://leetcode.com/problems/maximum-subsequence-score/

import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        idx = list(range(n))
        idx.sort(key=lambda i: -nums2[i])
        pq = []
        s = 0
        ans = 0
        for i in idx:
            heapq.heappush(pq, nums1[i])
            s += nums1[i]
            if len(pq) > k:
                s -= heapq.heappop(pq)
            if len(pq) == k:
                cand = s * nums2[i]
                if cand > ans:
                    ans = cand
        return ans
