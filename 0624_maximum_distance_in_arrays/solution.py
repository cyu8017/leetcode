# LeetCode 0624 - Maximum Distance in Arrays
# https://leetcode.com/problems/maximum-distance-in-arrays/

from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val, max_val = arrays[0][0], arrays[0][-1]
        best = 0
        for arr in arrays[1:]:
            best = max(best, abs(arr[-1] - min_val), abs(max_val - arr[0]))
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])
        return best
