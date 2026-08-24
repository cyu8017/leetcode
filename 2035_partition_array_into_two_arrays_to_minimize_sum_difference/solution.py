# LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total = sum(nums)
        left, right = nums[:n], nums[n:]

        def sums_by_count(arr: List[int]) -> List[List[int]]:
            m = len(arr)
            res = [[] for _ in range(m + 1)]
            for mask in range(1 << m):
                s = c = 0
                for i in range(m):
                    if mask & (1 << i):
                        s += arr[i]
                        c += 1
                res[c].append(s)
            for v in res:
                v.sort()
            return res

        L = sums_by_count(left)
        R = sums_by_count(right)
        ans = 10**18
        for k in range(n + 1):
            arr = R[n - k]
            for s1 in L[k]:
                need = total // 2 - s1
                lo, hi = 0, len(arr)
                while lo < hi:
                    mid = (lo + hi) >> 1
                    if arr[mid] < need:
                        lo = mid + 1
                    else:
                        hi = mid
                for j in (lo - 1, lo):
                    if 0 <= j < len(arr):
                        s2 = arr[j]
                        ans = min(ans, abs(total - 2 * (s1 + s2)))
        return ans
