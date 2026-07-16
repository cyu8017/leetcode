# LeetCode 0869 - Reordered Power of 2
# https://leetcode.com/problems/reordered-power-of-2/

from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = Counter(str(n))
        return any(Counter(str(1 << i)) == target for i in range(31))
