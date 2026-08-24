# LeetCode 3765 - Complete Prime Number
# https://leetcode.com/problems/complete-prime-number/

class Solution:
    def completePrime(self, num: int) -> bool:
        def isPrime(x: int) -> bool:
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        s = str(num)
        x = 0
        for c in s:
            x = x * 10 + (ord(c) - 48)
            if not isPrime(x):
                return False
        x = 0
        p = 1
        for i in range(len(s) - 1, -1, -1):
            x = p * (ord(s[i]) - 48) + x
            p *= 10
            if not isPrime(x):
                return False
        return True
