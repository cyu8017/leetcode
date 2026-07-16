from math import gcd

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(x, y): return x // gcd(x, y) * y
        ab, ac, bc = lcm(a, b), lcm(a, c), lcm(b, c)
        abc = lcm(ab, c)
        def count(x):
            return x // a + x // b + x // c - x // ab - x // ac - x // bc + x // abc
        lo, hi = 1, 2_000_000_000
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= n: hi = mid
            else: lo = mid + 1
        return lo
