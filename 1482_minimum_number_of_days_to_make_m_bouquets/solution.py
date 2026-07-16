from typing import List, Optional

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        def possible(day):
            bouquets = run = 0
            for x in bloomDay:
                run = run + 1 if x <= day else 0
                if run == k:
                    bouquets += 1; run = 0
            return bouquets >= m
        lo, hi = min(bloomDay), max(bloomDay)
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid): hi = mid
            else: lo = mid + 1
        return lo
