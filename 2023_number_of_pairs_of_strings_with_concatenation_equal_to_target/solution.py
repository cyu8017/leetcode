# LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    ans += 1
        return ans
