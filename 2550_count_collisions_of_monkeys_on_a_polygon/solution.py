# LeetCode 2550 - Count Collisions of Monkeys on a Polygon
# https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 1000000007

        def pow_mod(a: int, e: int) -> int:
            res = 1
            while e > 0:
                if e & 1:
                    res = res * a % MOD
                a = a * a % MOD
                e >>= 1
            return res

        return (pow_mod(2, n) - 2 + MOD) % MOD
