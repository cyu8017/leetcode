# LeetCode 3937 - Minimum Operations To Make Array Modulo Alternating I
# https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= k
        ans = 2147483647
        for x in range(k):
            for y in range(k):
                if x == y:
                    continue
                cnt = 0
                for i in range(len(nums)):
                    target = y if (i & 1) != 0 else x
                    diff = abs(target - nums[i])
                    cnt += min(diff, k - diff)
                ans = min(ans, cnt)
        return ans
