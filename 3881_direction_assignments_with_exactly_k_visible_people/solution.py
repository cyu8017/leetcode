# LeetCode 3881 - Direction Assignments With Exactly K Visible People
# https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

from typing import List, Optional

N3881 = 100001
MOD3881 = 1000000007
fact3881: Optional[List[int]] = None
invFact3881: Optional[List[int]] = None
ready3881 = False


def qmi3881(a: int, k: int, p: int) -> int:
    res = 1
    A = a
    K = k
    P = p
    while K != 0:
        if (K & 1) != 0:
            res = res * A % P
        K >>= 1
        A = A * A % P
    return res


def init3881() -> None:
    global fact3881, invFact3881, ready3881
    if ready3881:
        return
    fact3881 = [0] * N3881
    invFact3881 = [0] * N3881
    fact3881[0] = invFact3881[0] = 1
    for i in range(1, N3881):
        fact3881[i] = fact3881[i - 1] * i % MOD3881
        invFact3881[i] = qmi3881(fact3881[i], MOD3881 - 2, MOD3881)
    ready3881 = True


def comb3881(n: int, k: int) -> int:
    return fact3881[n] * invFact3881[k] % MOD3881 * invFact3881[n - k] % MOD3881


class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        init3881()
        l = pos
        r = n - pos - 1
        ans = 0
        for a in range(min(k, l) + 1):
            b = k - a
            if b <= r:
                ans = (ans + 2 * comb3881(l, a) % MOD3881 * comb3881(r, b) % MOD3881) % MOD3881
        return ans
