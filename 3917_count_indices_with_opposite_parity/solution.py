# LeetCode 3917 - Count Indices With Opposite Parity
# https://leetcode.com/problems/count-indices-with-opposite-parity/

from typing import List


class Solution:
    def countOppositeParity(self, nums: List[int]) -> List[int]:
        cnt = [0, 0]
        for x in nums:
            cnt[x & 1] += 1
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            x = nums[i]
            cnt[x & 1] -= 1
            ans[i] = cnt[(x & 1) ^ 1]
        return ans
