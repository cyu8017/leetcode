# LeetCode 2333 - Minimum Sum of Squared Difference
# https://leetcode.com/problems/minimum-sum-of-squared-difference/

from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [0] * n
        max_d = 0
        for i in range(n):
            d = abs(nums1[i] - nums2[i])
            diff[i] = d
            if d > max_d:
                max_d = d
        k = k1 + k2
        freq = [0] * (max_d + 1)
        for d in diff:
            freq[d] += 1
        for d in range(max_d, 0, -1):
            if k <= 0:
                break
            if freq[d] == 0:
                continue
            take = freq[d]
            if take > k:
                take = k
            freq[d] -= take
            freq[d - 1] += take
            k -= take
        ans = 0
        for d in range(max_d + 1):
            ans += d * d * freq[d]
        return ans
