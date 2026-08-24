# LeetCode 3595 - Once Twice
# https://leetcode.com/problems/once-twice/

from typing import List


class Solution:
    def onceTwice(self, nums: List[int]) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        a = b = 0
        for key, v in freq.items():
            if v == 1:
                a = key
            elif v == 2:
                b = key
        return [a, b]
