# LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        ans = 0
        for num in nums:
            dn = dp.get(num, 0)
            dnm1 = dp.get(num - 1, 0)
            dp[num + 1] = dn + 1
            dp[num] = dnm1 + 1
            ans = max(ans, max(dp[num], dp[num + 1]))
        return ans
