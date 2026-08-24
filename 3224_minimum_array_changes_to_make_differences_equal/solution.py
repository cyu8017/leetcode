# LeetCode 3224 - Minimum Array Changes to Make Differences Equal
# https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        d = [0] * (k + 2)
        n = len(nums)
        for i in range(n // 2):
            x, y = nums[i], nums[n - 1 - i]
            if x > y:
                x, y = y, x
            d[0] += 1
            d[y - x] -= 1
            d[y - x + 1] += 1
            mx = max(y, k - x)
            d[mx + 1] -= 1
            d[mx + 1] += 2
        ans, s = n, 0
        for x in d:
            s += x
            ans = min(ans, s)
        return ans
