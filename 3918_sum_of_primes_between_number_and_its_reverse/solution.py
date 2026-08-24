# LeetCode 3918 - Sum Of Primes Between Number And Its Reverse
# https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

from typing import List, Optional

isPrime3918: Optional[List[bool]] = None


def Init3918() -> None:
    global isPrime3918
    if isPrime3918 is not None:
        return
    isPrime3918 = [True] * 1001
    isPrime3918[0] = isPrime3918[1] = False
    i = 2
    while i * i <= 1000:
        if isPrime3918[i]:
            j = i * i
            while j <= 1000:
                isPrime3918[j] = False
                j += i
        i += 1


class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        Init3918()
        r = 0
        x = n
        while x > 0:
            r = r * 10 + x % 10
            x //= 10
        low = min(n, r)
        high = max(n, r)
        ans = 0
        for v in range(low, high + 1):
            if isPrime3918[v]:
                ans += v
        return ans
