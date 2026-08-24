# LeetCode 3825 - Longest Strictly Increasing Subsequence with Non Zero Bitwise AND
# https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

from typing import List


def bitLen(x: int) -> int:
    if x == 0:
        return 0
    n = 0
    while x > 0:
        n += 1
        x >>= 1
    return n


def lis(arr: List[int]) -> int:
    g = []
    for x in arr:
        lo, hi = 0, len(g)
        while lo < hi:
            mid = (lo + hi) >> 1
            if g[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(g):
            g.append(x)
        else:
            g[lo] = x
    return len(g)


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        mx = 0
        for x in nums:
            mx = max(mx, x)
        m = bitLen(mx)
        for i in range(m):
            arr = []
            for x in nums:
                if ((x >> i) & 1) != 0:
                    arr.append(x)
            ans = max(ans, lis(arr))
        return ans
