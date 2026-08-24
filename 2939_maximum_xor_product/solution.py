# LeetCode 2939 - Maximum Xor Product
# https://leetcode.com/problems/maximum-xor-product/


class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        mod = 1000000007
        A, B = a, b
        for i in range(n - 1, -1, -1):
            bit = 1 << i
            abit, bbit = A & bit, B & bit
            if abit == bbit:
                A |= bit
                B |= bit
            elif A > B:
                B |= bit
                A &= ~bit
            else:
                A |= bit
                B &= ~bit
        return ((A % mod) * (B % mod)) % mod
