# LeetCode 3731 - Find Missing Elements
# https://leetcode.com/problems/find-missing-elements/

from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn, mx = 100, 0
        s = set()
        for x in nums:
            mn = min(mn, x)
            mx = max(mx, x)
            s.add(x)
        ans = []
        for x in range(mn + 1, mx):
            if x not in s:
                ans.append(x)
        return ans
