# LeetCode 1318 - Minimum Flips To Make A Or B Equal To C

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            x, y, z = a & 1, b & 1, c & 1
            flips += (x + y if z == 0 else int(x == 0 and y == 0))
            a >>= 1; b >>= 1; c >>= 1
        return flips
