# LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        idx = list(range(n))
        idx.sort(key=lambda i: nums[i])
        ans = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[idx[j]] - nums[idx[j - 1]] <= limit:
                j += 1
            group_idx = idx[i:j]
            group_idx.sort()
            for t in range(j - i):
                ans[group_idx[t]] = nums[idx[i + t]]
            i = j
        return ans
