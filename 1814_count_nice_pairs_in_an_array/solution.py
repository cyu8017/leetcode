# LeetCode 1814 - Count Nice Pairs in an Array
# https://leetcode.com/problems/count-nice-pairs-in-an-array/

from collections import Counter
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        freq = Counter()
        ans = 0

        for num in nums:
            diff = num - self._rev(num)
            ans = (ans + freq[diff]) % mod
            freq[diff] += 1

        return ans

    def _rev(self, x: int) -> int:
        return int(str(x)[::-1])
