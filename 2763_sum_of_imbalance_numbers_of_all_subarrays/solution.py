# LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
# https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

from typing import List


class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            seen = set()
            sorted_vals = []
            imbalance = 0

            def ceil_idx(x: int) -> int:
                lo, hi = 0, len(sorted_vals)
                while lo < hi:
                    mid = (lo + hi) >> 1
                    if sorted_vals[mid] < x:
                        lo = mid + 1
                    else:
                        hi = mid
                return lo

            for j in range(i, n):
                x = nums[j]
                if x not in seen:
                    seen.add(x)
                    idx = ceil_idx(x)
                    nxt = sorted_vals[idx] if idx < len(sorted_vals) else None
                    prev = sorted_vals[idx - 1] if idx > 0 else None
                    if prev is not None and x - prev != 1:
                        imbalance += 1
                    if nxt is not None and nxt - x != 1:
                        imbalance += 1
                    if prev is not None and nxt is not None and nxt - prev > 1:
                        imbalance -= 1
                    sorted_vals.insert(idx, x)
                ans += imbalance
        return ans
