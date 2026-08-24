# LeetCode 3748 - Count Stable Subarrays
# https://leetcode.com/problems/count-stable-subarrays/

from typing import List


class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg = []
        s = [0]
        l = 0
        for r in range(n):
            if r == n - 1 or nums[r] > nums[r + 1]:
                seg.append(l)
                k = r - l + 1
                s.append(s[-1] + k * (k + 1) // 2)
                l = r + 1

        def lowerBound(a: List[int], x: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        ans = [0] * len(queries)
        for idx, (left, right) in enumerate(queries):
            i = lowerBound(seg, left + 1)
            j = lowerBound(seg, right + 1) - 1
            if i > j:
                k = right - left + 1
                ans[idx] = k * (k + 1) // 2
            else:
                a = seg[i] - left
                b = right - seg[j] + 1
                ans[idx] = a * (a + 1) // 2 + s[j] - s[i] + b * (b + 1) // 2
        return ans
