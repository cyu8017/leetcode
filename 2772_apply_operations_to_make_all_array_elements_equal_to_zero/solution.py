# LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
# https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        cur = 0
        for i in range(n):
            cur += diff[i]
            need = nums[i] - cur
            if need < 0:
                return False
            if need > 0:
                if i + k > n:
                    return False
                cur += need
                diff[i + k] -= need
        return True
