# LeetCode 2426 - Number of Pairs Satisfying Inequality
# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        arr = [nums1[i] - nums2[i] for i in range(n)]
        tmp = [0] * n

        def merge_count(l: int, r: int) -> int:
            if r - l <= 1:
                return 0
            m = (l + r) >> 1
            ans = merge_count(l, m) + merge_count(m, r)
            j = m
            for i in range(l, m):
                while j < r and arr[j] < arr[i] - diff:
                    j += 1
                ans += r - j
            p, q, i2 = l, m, l
            while p < m and q < r:
                if arr[p] <= arr[q]:
                    tmp[i2] = arr[p]
                    p += 1
                else:
                    tmp[i2] = arr[q]
                    q += 1
                i2 += 1
            while p < m:
                tmp[i2] = arr[p]
                p += 1
                i2 += 1
            while q < r:
                tmp[i2] = arr[q]
                q += 1
                i2 += 1
            for t in range(l, r):
                arr[t] = tmp[t]
            return ans

        return merge_count(0, n)
