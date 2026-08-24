# LeetCode 3254 - Find the Power of K-Size Subarrays I
# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        for i in range(n - k + 1):
            ok = True
            for j in range(i + 1, i + k):
                if nums[j] != nums[j - 1] + 1:
                    ok = False
                    break
            ans[i] = nums[i + k - 1] if ok else -1
        return ans
