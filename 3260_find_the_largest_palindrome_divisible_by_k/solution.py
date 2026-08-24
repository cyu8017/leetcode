# LeetCode 3260 - Find the Largest Palindrome Divisible by K
# https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

from typing import List


class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        def repeat(c: str, n: int) -> List[str]:
            return [c] * n

        digits = repeat("9", n)
        half = (n + 1) // 2

        def mod7(s: str) -> int:
            r = 0
            for i in range(len(s)):
                r = (r * 10 + (ord(s[i]) - 48)) % 7
            return r

        def largestPal7(n: int) -> str:
            halfLen = (n + 1) // 2
            half = repeat("9", halfLen)
            while True:
                pal = [""] * n
                for i in range(halfLen):
                    pal[i] = half[i]
                for i in range(n // 2):
                    pal[n - 1 - i] = pal[i]
                if mod7("".join(pal)) == 0:
                    return "".join(pal)
                idx = halfLen - 1
                while idx >= 0 and half[idx] == "0":
                    half[idx] = "9"
                    idx -= 1
                if idx < 0:
                    break
                half[idx] = chr(ord(half[idx]) - 1)
            return ""

        if k in (1, 3, 9):
            return "".join(digits)
        if k == 2:
            digits[0] = digits[n - 1] = "8"
            return "".join(digits)
        if k == 4:
            if n == 1:
                return "8"
            digits[0] = digits[1] = digits[n - 1] = digits[n - 2] = "8"
            return "".join(digits)
        if k == 5:
            digits[0] = digits[n - 1] = "5"
            return "".join(digits)
        if k == 8:
            if n <= 2:
                return "".join(repeat("8", n))
            digits[0] = digits[1] = digits[2] = "8"
            digits[n - 1] = digits[n - 2] = digits[n - 3] = "8"
            return "".join(digits)
        if k == 6:
            if n == 1:
                return "6"
            digits[0] = digits[n - 1] = "8"
            ssum = 16 + 9 * (n - 2)
            need = ssum % 3
            if need != 0:
                pos = half - 1
                digits[pos] = chr(ord(digits[pos]) - need)
                if n % 2 == 0 or pos != n - 1 - pos:
                    digits[n - 1 - pos] = digits[pos]
            return "".join(digits)
        if k == 7:
            return largestPal7(n)
        return "".join(digits)
