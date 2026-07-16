# LeetCode 0972 - Equal Rational Numbers
# https://leetcode.com/problems/equal-rational-numbers/

from fractions import Fraction


class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse(x: str) -> Fraction:
            if "(" not in x:
                return Fraction(x) if x else Fraction(0)
            non_rep, rest = x.split("(")
            rep = rest[:-1]
            if "." not in non_rep:
                non_rep += "."
            integer, frac = non_rep.split(".")
            base = Fraction(int(integer or "0"))
            if frac:
                base += Fraction(int(frac), 10 ** len(frac))
            if rep:
                base += Fraction(int(rep), (10 ** len(rep) - 1) * 10 ** len(frac))
            return base

        return parse(s) == parse(t)
