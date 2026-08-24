# LeetCode 2214 - Minimum Health to Beat Game
# https://leetcode.com/problems/minimum-health-to-beat-game/

from typing import List
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        sum = 0
        mx = 0
        for d in damage:
            sum += d
            mx = max(mx, d)
        return sum - min(armor, mx) + 1
