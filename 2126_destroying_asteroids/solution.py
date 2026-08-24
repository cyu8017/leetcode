# LeetCode 2126 - Destroying Asteroids
# https://leetcode.com/problems/destroying-asteroids/

from typing import List
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)
        cur = mass
        for a in asteroids:
            if cur < a:
                return False
            cur += a
        return True
