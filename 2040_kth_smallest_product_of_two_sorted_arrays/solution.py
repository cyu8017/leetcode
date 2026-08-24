# LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_le(x: int) -> int:
            cnt = 0
            for a in nums1:
                if a > 0:
                    lo, hi = 0, len(nums2)
                    while lo < hi:
                        mid = (lo + hi) >> 1
                        if a * nums2[mid] <= x:
                            lo = mid + 1
                        else:
                            hi = mid
                    cnt += lo
                elif a < 0:
                    lo, hi = 0, len(nums2)
                    while lo < hi:
                        mid = (lo + hi) >> 1
                        if a * nums2[mid] <= x:
                            hi = mid
                        else:
                            lo = mid + 1
                    cnt += len(nums2) - lo
                elif x >= 0:
                    cnt += len(nums2)
            return cnt

        lo, hi = -10**10, 10**10
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
