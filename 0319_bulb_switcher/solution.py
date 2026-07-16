# LeetCode 0319 - Bulb Switcher
# https://leetcode.com/problems/bulb-switcher/

import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.isqrt(n))
