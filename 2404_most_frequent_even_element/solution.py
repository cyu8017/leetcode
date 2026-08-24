# LeetCode 2404 - Most Frequent Even Element
# https://leetcode.com/problems/most-frequent-even-element/

from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        cnt = {}
        ans = -1
        best = 0
        for x in nums:
            if x % 2 != 0:
                continue
            c = cnt.get(x, 0) + 1
            cnt[x] = c
            if c > best or (c == best and (ans == -1 or x < ans)):
                best = c
                ans = x
        return ans
