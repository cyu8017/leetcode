# LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        cnt = [0] * 51
        ans = 0
        for x in nums:
            cnt[x] += 1
            if cnt[x] == 2:
                ans ^= x
        return ans
