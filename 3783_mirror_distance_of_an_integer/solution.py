# LeetCode 3783 - Mirror Distance of an Integer
# https://leetcode.com/problems/mirror-distance-of-an-integer/

class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(x: int) -> int:
            y = 0
            while x > 0:
                y = y * 10 + x % 10
                x //= 10
            return y

        return abs(n - reverse(n))
