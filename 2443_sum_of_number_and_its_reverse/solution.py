# LeetCode 2443 - Sum of Number and Its Reverse
# https://leetcode.com/problems/sum-of-number-and-its-reverse/


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def rev(x: int) -> int:
            r = 0
            while x > 0:
                r = r * 10 + x % 10
                x //= 10
            return r

        for i in range(num + 1):
            if i + rev(i) == num:
                return True
        return False
