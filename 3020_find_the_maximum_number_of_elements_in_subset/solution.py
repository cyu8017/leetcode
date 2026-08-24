# LeetCode 3020 - Find the Maximum Number of Elements in Subset
# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        ones = cnt.get(1, 0)
        ans = ones - ((ones % 2) ^ 1)
        if 1 in cnt:
            del cnt[1]
        keys = list(cnt.keys())
        for start in keys:
            x = start
            t = 0
            while cnt.get(x, 0) > 1:
                x = x * x
                t += 2
            if cnt.get(x, 0) > 0:
                t += 1
            else:
                t -= 1
            ans = max(ans, t)
        return ans
