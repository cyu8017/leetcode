# LeetCode 3524 - Find X Value of Array I
# https://leetcode.com/problems/find-x-value-of-array-i/

from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        for num in nums:
            new_dp = [0] * k
            nm = num % k
            new_dp[nm] = 1
            for i in range(k):
                new_dp[(i * nm) % k] += dp[i]
            for i in range(k):
                ans[i] += new_dp[i]
            dp = new_dp
        return ans
