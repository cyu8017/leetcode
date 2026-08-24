# LeetCode 2543 - Check if Point Is Reachable
# https://leetcode.com/problems/check-if-point-is-reachable/

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        g = gcd(targetX, targetY)
        while g % 2 == 0:
            g //= 2
        return g == 1
