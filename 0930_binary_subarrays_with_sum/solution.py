# LeetCode 0930 - Binary Subarrays With Sum
# https://leetcode.com/problems/binary-subarrays-with-sum/

from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix = 0
        count: dict[int, int] = defaultdict(int)
        count[0] = 1
        ans = 0
        for x in nums:
            prefix += x
            ans += count[prefix - goal]
            count[prefix] += 1
        return ans
