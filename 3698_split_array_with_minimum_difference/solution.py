# LeetCode 3698 - Split Array With Minimum Difference
# https://leetcode.com/problems/split-array-with-minimum-difference/

from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0] * n
        f = [True] * n
        g = [True] * n
        s[0] = nums[0]
        for i in range(1, n):
            s[i] = s[i - 1] + nums[i]
            f[i] = f[i - 1]
            if nums[i] <= nums[i - 1]:
                f[i] = False
        for i in range(n - 2, -1, -1):
            g[i] = g[i + 1]
            if nums[i] <= nums[i + 1]:
                g[i] = False
        inf = 10**18
        ans = inf
        for i in range(n - 1):
            if f[i] and g[i + 1]:
                s1, s2 = s[i], s[n - 1] - s[i]
                ans = min(ans, abs(s1 - s2))
        return ans if ans < inf else -1
