# LeetCode 1182 - Shortest Distance to Target Color
# https://leetcode.com/problems/shortest-distance-to-target-color/

from collections import defaultdict
import bisect


class Solution:
    def shortestDistanceColor(self, colors: list[int], queries: list[list[int]]) -> list[int]:
        pos: dict[int, list[int]] = defaultdict(list)
        for i, c in enumerate(colors):
            pos[c].append(i)
        ans = []
        for i, c in queries:
            if c not in pos:
                ans.append(-1)
                continue
            arr = pos[c]
            idx = bisect.bisect_left(arr, i)
            best = float("inf")
            if idx < len(arr):
                best = min(best, arr[idx] - i)
            if idx:
                best = min(best, i - arr[idx - 1])
            ans.append(best if best != float("inf") else -1)
        return ans
