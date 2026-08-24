# LeetCode 3728 - Stable Subarrays With Equal Boundary and Interior Sum
# https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

from typing import List


class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        s = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = s[i - 1] + capacity[i - 1]
        cnt = {}
        ans = 0
        for r in range(2, n):
            l = r - 2
            key_l = (capacity[l], capacity[l] + s[l + 1])
            cnt[key_l] = cnt.get(key_l, 0) + 1
            key_r = (capacity[r], s[r])
            ans += cnt.get(key_r, 0)
        return ans
