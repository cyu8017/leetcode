# LeetCode 0786 - K-th Smallest Prime Fraction
# https://leetcode.com/problems/k-th-smallest-prime-fraction/

import heapq
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = [(arr[i] / arr[-1], i, n - 1) for i in range(n - 1)]
        heapq.heapify(heap)
        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
            if j - 1 > i:
                heapq.heappush(heap, (arr[i] / arr[j - 1], i, j - 1))
        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]
