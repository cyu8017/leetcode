# LeetCode 2515 - Shortest Distance to Target String in a Circular Array
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        best = -1
        for i in range(n):
            if words[i] == target:
                d = i - startIndex
                if d < 0:
                    d = -d
                if n - d < d:
                    d = n - d
                if best < 0 or d < best:
                    best = d
        return best
