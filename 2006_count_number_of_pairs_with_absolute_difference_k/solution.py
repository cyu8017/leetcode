# LeetCode 2006 - Count Number of Pairs With Absolute Difference K
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = {}
        ans = 0
        for x in nums:
            ans += freq.get(x - k, 0)
            ans += freq.get(x + k, 0)
            freq[x] = freq.get(x, 0) + 1
        return ans
