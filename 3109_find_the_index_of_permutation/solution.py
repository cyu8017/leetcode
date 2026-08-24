# LeetCode 3109 - Find the Index of Permutation
# https://leetcode.com/problems/find-the-index-of-permutation/

from typing import List


class BIT:
    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, delta: int) -> None:
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s


class Solution:
    def getPermutationIndex(self, perm: List[int]) -> int:
        MOD = 1000000007
        n = len(perm)
        tree = BIT(n + 1)
        f = [0] * n
        f[0] = 1
        for i in range(1, n):
            f[i] = f[i - 1] * i % MOD
        ans = 0
        for i in range(n):
            x = perm[i]
            cnt = x - 1 - tree.query(x)
            ans = (ans + cnt * f[n - 1 - i]) % MOD
            tree.update(x, 1)
        return ans
