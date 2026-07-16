# LeetCode 0770 - Basic Calculator IV
# https://leetcode.com/problems/basic-calculator-iv/

from collections import Counter
from typing import List


class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: List[str], evalints: List[int]
    ) -> List[str]:
        values = dict(zip(evalvars, evalints))
        tokens = expression.replace("(", " ( ").replace(")", " ) ").split()
        pos = 0

        def parse_expr() -> Counter:
            nonlocal pos
            poly = parse_term()
            while pos < len(tokens) and tokens[pos] in {"+", "-"}:
                op = tokens[pos]
                pos += 1
                right = parse_term()
                if op == "+":
                    poly = add(poly, right)
                else:
                    poly = add(poly, negate(right))
            return poly

        def parse_term() -> Counter:
            nonlocal pos
            poly = parse_factor()
            while pos < len(tokens) and tokens[pos] == "*":
                pos += 1
                poly = mul(poly, parse_factor())
            return poly

        def parse_factor() -> Counter:
            nonlocal pos
            token = tokens[pos]
            if token == "(":
                pos += 1
                poly = parse_expr()
                pos += 1  # ')'
                return poly
            pos += 1
            return atom(token)

        def atom(token: str) -> Counter:
            poly: Counter = Counter()
            if token.isalpha():
                if token in values:
                    poly[()] = values[token]
                else:
                    poly[(token,)] = 1
            else:
                poly[()] = int(token)
            return poly

        def add(left: Counter, right: Counter) -> Counter:
            result = Counter(left)
            for key, coef in right.items():
                result[key] += coef
            return Counter({k: v for k, v in result.items() if v})

        def negate(poly: Counter) -> Counter:
            return Counter({k: -v for k, v in poly.items()})

        def mul(left: Counter, right: Counter) -> Counter:
            result: Counter = Counter()
            for lk, lv in left.items():
                for rk, rv in right.items():
                    key = tuple(sorted(lk + rk))
                    result[key] += lv * rv
            return Counter({k: v for k, v in result.items() if v})

        poly = parse_expr()
        keys = sorted(poly.keys(), key=lambda k: (-len(k), k))
        answer: list[str] = []
        for key in keys:
            coef = poly[key]
            if not key:
                answer.append(str(coef))
            else:
                answer.append("*".join([str(coef), *key]))
        return answer
