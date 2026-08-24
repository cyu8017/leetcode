# LeetCode 2638 - Count the Number of K-Free Subsets
# https://leetcode.com/problems/count-the-number-of-k-free-subsets/

from typing import List


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        groups = {}
        for x in nums:
            key = x % k
            if key not in groups:
                groups[key] = []
            groups[key].append(x)
        ans = 1
        for g in groups.values():
            prev_val = -1
            prev_take = 0
            prev_skip = 1
            for v in g:
                skip = prev_take + prev_skip
                take = prev_skip if prev_val + k == v else prev_take + prev_skip
                prev_take = take
                prev_skip = skip
                prev_val = v
            ans *= prev_take + prev_skip
        return ans
