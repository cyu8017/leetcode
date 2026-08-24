# LeetCode 2857 - Count Pairs of Points With Distance k
# https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

from typing import List


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        freq = {}
        ans = 0
        for x, y in coordinates:
            for a in range(k + 1):
                b = k - a
                ans += freq.get((x ^ a, y ^ b), 0)
            key = (x, y)
            freq[key] = freq.get(key, 0) + 1
        return ans
