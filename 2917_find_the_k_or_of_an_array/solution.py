# LeetCode 2917 - Find the K-or of an Array
# https://leetcode.com/problems/find-the-k-or-of-an-array/

from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        for b in range(31):
            cnt = 0
            for v in nums:
                if (v & (1 << b)) != 0:
                    cnt += 1
            if cnt >= k:
                ans |= 1 << b
        return ans
