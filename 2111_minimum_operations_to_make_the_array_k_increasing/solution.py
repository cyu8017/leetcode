# LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
# https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

from typing import List
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        ans = 0
        n = len(arr)
        for start in range(k):
            seq = []
            for i in range(start, n, k):
                seq.append(arr[i])
            tails = []
            for x in seq:
                lo = 0
                hi = len(tails)
                while lo < hi:
                    mid = (lo + hi) >> 1
                    if tails[mid] <= x:
                        lo = mid + 1
                    else:
                        hi = mid
                if lo == len(tails):
                    tails.append(x)
                else:
                    tails[lo] = x
            ans += len(seq) - len(tails)
        return ans
