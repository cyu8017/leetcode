# LeetCode 1090 - Largest Values From Labels
# https://leetcode.com/problems/largest-values-from-labels/

from collections import defaultdict


class Solution:
    def largestValsFromLabels(
        self, values: list[int], labels: list[int], numWanted: int, useLimit: int
    ) -> int:
        items = sorted(zip(values, labels), reverse=True)
        used: dict[int, int] = defaultdict(int)
        ans = taken = 0
        for value, label in items:
            if taken == numWanted:
                break
            if used[label] < useLimit:
                used[label] += 1
                ans += value
                taken += 1
        return ans
