# LeetCode 2841 - Maximum Sum of Almost Unique Subarray
# https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        freq = {}
        total = 0
        ans = 0
        for i, v in enumerate(nums):
            freq[v] = freq.get(v, 0) + 1
            total += v
            if i >= k:
                out = nums[i - k]
                total -= out
                c = freq.get(out, 0) - 1
                if c == 0:
                    del freq[out]
                else:
                    freq[out] = c
            if i >= k - 1 and len(freq) >= m:
                ans = max(ans, total)
        return ans
