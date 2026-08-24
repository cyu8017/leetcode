# LeetCode 3852 - Smallest Pair With Different Frequencies
# https://leetcode.com/problems/smallest-pair-with-different-frequencies/

from typing import Dict, List


class Solution:
    def minDistinctFreqPair(self, nums: List[int]) -> List[int]:
        cnt: Dict[int, int] = {}
        for v in nums:
            cnt[v] = cnt.get(v, 0) + 1
        x = nums[0]
        for v in nums:
            x = min(x, v)
        min_y = float("inf")
        for y in cnt:
            if y < min_y and cnt[x] != cnt[y]:
                min_y = y
        if min_y == float("inf"):
            return [-1, -1]
        return [x, int(min_y)]
