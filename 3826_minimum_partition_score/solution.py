# LeetCode 3826 - Minimum Partition Score
# https://leetcode.com/problems/minimum-partition-score/

from typing import List


class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF = 10**18
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        previous = [INF] * (n + 1)
        previous[0] = 0

        def value(left: int, right: int) -> int:
            s = prefix[right] - prefix[left]
            return s * (s + 1) // 2

        current: List[int] = []

        def compute(lo: int, hi: int, optLo: int, optHi: int) -> None:
            if lo > hi:
                return
            mid = (lo + hi) >> 1
            bestIndex = -1
            end = min(optHi, mid - 1)
            for split in range(optLo, end + 1):
                if previous[split] == INF:
                    continue
                candidate = previous[split] + value(split, mid)
                if candidate < current[mid]:
                    current[mid] = candidate
                    bestIndex = split
            if bestIndex == -1:
                bestIndex = optLo
            compute(lo, mid - 1, optLo, bestIndex)
            compute(mid + 1, hi, bestIndex, optHi)

        for parts in range(1, k + 1):
            current = [INF] * (n + 1)
            compute(parts, n, parts - 1, n - 1)
            previous = current
        return previous[n]
