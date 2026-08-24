# LeetCode 3916 - Number of ZigZag Arrays III
# https://leetcode.com/problems/number-of-zigzag-arrays-iii/

from typing import List


def powm3916(a: int, e: int, mod: int) -> int:
    res = 1
    A = a
    E = e
    MOD = mod
    while E > 0:
        if (E & 1) != 0:
            res = res * A % MOD
        A = A * A % MOD
        E >>= 1
    return res


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 1000000007
        points = n + 1
        values = [0] * (points + 1)
        for m in range(1, points + 1):
            up = [0] * m
            down = [0] * m
            for value in range(m):
                up[value] = value
                down[value] = m - 1 - value
            for _length in range(3, n + 1):
                next_up = [0] * m
                next_down = [0] * m
                prefix = 0
                for value in range(m):
                    next_up[value] = prefix
                    prefix = (prefix + down[value]) % mod
                suffix = 0
                for value in range(m - 1, -1, -1):
                    next_down[value] = suffix
                    suffix = (suffix + up[value]) % mod
                up = next_up
                down = next_down
            for value in range(m):
                values[m] = (values[m] + up[value] + down[value]) % mod
        x = (r - l + 1) % mod
        if r - l + 1 <= points:
            return values[r - l + 1]
        prefix_a = [0] * (points + 2)
        suffix_a = [0] * (points + 2)
        prefix_a[0] = 1
        for i in range(1, points + 1):
            prefix_a[i] = prefix_a[i - 1] * ((x - i + mod) % mod) % mod
        suffix_a[points + 1] = 1
        for i in range(points, 0, -1):
            suffix_a[i] = suffix_a[i + 1] * ((x - i + mod) % mod) % mod
        factorial = [0] * (points + 1)
        factorial[0] = 1
        for i in range(1, points + 1):
            factorial[i] = factorial[i - 1] * i % mod
        answer = 0
        for i in range(1, points + 1):
            numerator = prefix_a[i - 1] * suffix_a[i + 1] % mod
            denominator = factorial[i - 1] * factorial[points - i] % mod
            term = values[i] * numerator % mod * powm3916(denominator, mod - 2, mod) % mod
            if (points - i) % 2 == 1:
                answer -= term
            else:
                answer += term
            answer %= mod
        if answer < 0:
            answer += mod
        return answer
