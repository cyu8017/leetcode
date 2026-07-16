# LeetCode 0325 - Maximum Size Subarray Sum Equals k
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_index = {0: -1}
        prefix = 0
        best = 0
        for index, num in enumerate(nums):
            prefix += num
            if prefix - k in prefix_index:
                best = max(best, index - prefix_index[prefix - k])
            if prefix not in prefix_index:
                prefix_index[prefix] = index
        return best
