# LeetCode 3842 - Toggle Light Bulbs
# https://leetcode.com/problems/toggle-light-bulbs/

from typing import List


class Solution:
    def toggleLightBulbs(self, bulbs: List[int]) -> List[int]:
        st = [0] * 101
        for x in bulbs:
            st[x] ^= 1
        ans = []
        for i in range(101):
            if st[i] == 1:
                ans.append(i)
        return ans
