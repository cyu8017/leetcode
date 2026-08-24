# LeetCode 3206 - Alternating Groups I
# https://leetcode.com/problems/alternating-groups-i/

from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        k, n = 3, len(colors)
        cnt, ans = 0, 0
        for i in range(n * 2):
            if i > 0 and colors[i % n] == colors[(i - 1) % n]:
                cnt = 1
            else:
                cnt += 1
            if i >= n and cnt >= k:
                ans += 1
        return ans
