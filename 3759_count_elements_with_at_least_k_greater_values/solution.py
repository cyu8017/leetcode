# LeetCode 3759 - Count Elements with at Least K Greater Values
# https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

from typing import List


class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return n
        a = sorted(nums)
        ans = 0
        for i in range(n - k):
            if a[n - k] > a[i]:
                ans += 1
        return ans
