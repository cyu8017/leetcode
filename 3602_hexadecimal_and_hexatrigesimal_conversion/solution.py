# LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
# https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/


def f3602(x: int, k: int) -> str:
    res = []
    while x > 0:
        v = x % k
        res.append(chr(48 + v) if v <= 9 else chr(65 + v - 10))
        x //= k
    return "".join(reversed(res))


class Solution:
    def concatHex36(self, n: int) -> str:
        return f3602(n * n, 16) + f3602(n * n * n, 36)
