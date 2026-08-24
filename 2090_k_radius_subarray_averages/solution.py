# LeetCode 2090 - K Radius Subarray Averages
# https://leetcode.com/problems/k-radius-subarray-averages/

from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        if 2 * k + 1 > n:
            return ans
        window = 2 * k + 1
        s = sum(nums[:window])
        ans[k] = s // window
        for i in range(k + 1, n - k):
            s += nums[i + k] - nums[i - k - 1]
            ans[i] = s // window
        return ans
