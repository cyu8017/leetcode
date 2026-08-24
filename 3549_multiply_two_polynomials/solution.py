# LeetCode 3549 - Multiply Two Polynomials
# https://leetcode.com/problems/multiply-two-polynomials/

import math
from typing import List


class Complex:
    def __init__(self, re: float, im: float) -> None:
        self.re = re
        self.im = im

    def mul(self, o: "Complex") -> "Complex":
        return Complex(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def add(self, o: "Complex") -> "Complex":
        return Complex(self.re + o.re, self.im + o.im)

    def sub(self, o: "Complex") -> "Complex":
        return Complex(self.re - o.re, self.im - o.im)

    def div(self, x: float) -> "Complex":
        return Complex(self.re / x, self.im / x)


def fft(a: List[Complex], invert: bool) -> None:
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while (j & bit) != 0:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        angle = 2 * math.pi / length * (-1 if invert else 1)
        wlen = Complex(math.cos(angle), math.sin(angle))
        for i in range(0, n, length):
            w = Complex(1, 0)
            half = length >> 1
            for jj in range(half):
                u = a[i + jj]
                v = a[i + jj + half].mul(w)
                a[i + jj] = u.add(v)
                a[i + jj + half] = u.sub(v)
                w = w.mul(wlen)
        length <<= 1
    if invert:
        for i in range(n):
            a[i] = a[i].div(n)


class Solution:
    def multiply(self, poly1: List[int], poly2: List[int]) -> List[int]:
        if not poly1 or not poly2:
            return []
        m = len(poly1) + len(poly2) - 1
        n = 1
        while n < m:
            n <<= 1
        fa = [Complex(0, 0) for _ in range(n)]
        fb = [Complex(0, 0) for _ in range(n)]
        for i in range(n):
            fa[i] = Complex(poly1[i] if i < len(poly1) else 0, 0)
            fb[i] = Complex(poly2[i] if i < len(poly2) else 0, 0)
        fft(fa, False)
        fft(fb, False)
        for i in range(n):
            fa[i] = fa[i].mul(fb[i])
        fft(fa, True)
        return [int(round(fa[i].re)) for i in range(m)]
