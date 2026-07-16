# LeetCode 0858 - Mirror Reflection
# https://leetcode.com/problems/mirror-reflection/

import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p, q)
        p //= g
        q //= g
        if p % 2 == 0:
            return 2
        if q % 2 == 0:
            return 0
        return 1
