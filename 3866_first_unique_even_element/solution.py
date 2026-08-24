# LeetCode 3866 - First Unique Even Element
# https://leetcode.com/problems/first-unique-even-element/

from typing import List


class Solution:
    def firstUniqueEven(self, nums: List[int]) -> int:
        cnt = [0] * 101
        for x in nums:
            cnt[x] += 1
        for x in nums:
            if x % 2 == 0 and cnt[x] == 1:
                return x
        return -1
