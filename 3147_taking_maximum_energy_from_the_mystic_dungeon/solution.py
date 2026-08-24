# LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = -(1 << 30)
        n = len(energy)
        for i in range(n - k, n):
            s = 0
            j = i
            while j >= 0:
                s += energy[j]
                ans = max(ans, s)
                j -= k
        return ans
