from math import gcd

class Solution:
    def simplifiedFractions(self, n):
        return [f"{a}/{b}" for a in range(1, n) for b in range(a + 1, n + 1) if gcd(a, b) == 1]
