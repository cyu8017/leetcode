# LeetCode 0667 - Beautiful Arrangement II
# https://leetcode.com/problems/beautiful-arrangement-ii/

from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = list(range(1, n - k + 1))
        left, right = n - k + 1, n
        take_high = True
        while left <= right:
            if take_high:
                res.append(right)
                right -= 1
            else:
                res.append(left)
                left += 1
            take_high = not take_high
        return res
