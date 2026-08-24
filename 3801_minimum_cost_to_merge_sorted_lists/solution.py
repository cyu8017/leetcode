# LeetCode 3801 - Minimum Cost to Merge Sorted Lists
# https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

from typing import List


class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        m = len(lists)
        totalMasks = 1 << m
        merged = [[] for _ in range(totalMasks)]
        length = [0] * totalMasks
        median = [0] * totalMasks

        def trailingZeros(bit: int) -> int:
            n = 0
            while (bit & 1) == 0:
                bit >>= 1
                n += 1
            return n

        for mask in range(1, totalMasks):
            bit = mask & -mask
            index = trailingZeros(bit)
            previous = merged[mask ^ bit]
            current = lists[index]
            out = []
            i = j = 0
            while i < len(previous) or j < len(current):
                if j == len(current) or (i < len(previous) and previous[i] <= current[j]):
                    out.append(previous[i])
                    i += 1
                else:
                    out.append(current[j])
                    j += 1
            merged[mask] = out
            length[mask] = len(out)
            median[mask] = out[(len(out) - 1) // 2]
        INF = 10**18
        dp = [0] * totalMasks
        for mask in range(1, totalMasks):
            if (mask & (mask - 1)) == 0:
                continue
            dp[mask] = INF
            firstBit = mask & -mask
            left = (mask - 1) & mask
            while left > 0:
                if (left & firstBit) != 0:
                    right = mask ^ left
                    if right != 0:
                        diff = median[left] - median[right]
                        if diff < 0:
                            diff = -diff
                        candidate = dp[left] + dp[right] + length[mask] + diff
                        if candidate < dp[mask]:
                            dp[mask] = candidate
                left = (left - 1) & mask
        return dp[totalMasks - 1]
