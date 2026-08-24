# LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = [(v, i) for i, v in enumerate(nums)]
        arr.sort(key=lambda x: -x[0])
        idx = sorted(x[1] for x in arr[:k])
        return [nums[i] for i in idx]
