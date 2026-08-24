# LeetCode 3354 - Make Array Elements Equal to Zero
# https://leetcode.com/problems/make-array-elements-equal-to-zero/

from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] != 0:
                continue
            for direction in (-1, 1):
                a = nums[:]
                cur, d = i, direction
                while 0 <= cur < n:
                    if a[cur] == 0:
                        cur += d
                    else:
                        a[cur] -= 1
                        d = -d
                        cur += d
                if all(v == 0 for v in a):
                    ans += 1
        return ans
