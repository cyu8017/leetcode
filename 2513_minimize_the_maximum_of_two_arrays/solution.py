# LeetCode 2513 - Minimize the Maximum of Two Arrays
# https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/


class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        lcm = (divisor1 // gcd(divisor1, divisor2)) * divisor2

        def ok(x: int) -> bool:
            a = x - x // divisor1
            b = x - x // divisor2
            both = x - x // lcm
            return a >= uniqueCnt1 and b >= uniqueCnt2 and both >= uniqueCnt1 + uniqueCnt2

        lo, hi = 1, 2**62
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
