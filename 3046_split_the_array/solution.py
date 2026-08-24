# LeetCode 3046 - Split the Array
# https://leetcode.com/problems/split-the-array/

from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        cnt = [0] * 101
        for x in nums:
            cnt[x] += 1
            if cnt[x] >= 3:
                return False
        return True
