# LeetCode 0866 - Prime Palindrome
# https://leetcode.com/problems/prime-palindrome/

class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            d = 3
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 2
            return True

        def pals() -> int:
            # odd-length palindromes (even length > 11 are divisible by 11)
            for length in range(1, 6):
                start = 10 ** (length - 1)
                end = 10 ** length
                for root in range(start, end):
                    s = str(root)
                    pal = int(s + s[-2::-1])
                    if pal >= n and is_prime(pal):
                        return pal
            return 0

        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11
        return pals()
