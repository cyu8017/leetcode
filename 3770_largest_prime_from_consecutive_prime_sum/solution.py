# LeetCode 3770 - Largest Prime from Consecutive Prime Sum
# https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

class Solution:
    def largestPrime(self, n: int) -> int:
        MX = 500000
        isPrime = [True] * (MX + 1)
        isPrime[0] = isPrime[1] = False
        primes = []
        for i in range(2, MX + 1):
            if isPrime[i]:
                primes.append(i)
                if i * i <= MX:
                    for j in range(i * i, MX + 1, i):
                        isPrime[j] = False
        S = [0]
        t = 0
        for x in primes:
            t += x
            if t > MX:
                break
            if isPrime[t]:
                S.append(t)
        lo, hi = 0, len(S)
        while lo < hi:
            mid = (lo + hi) >> 1
            if S[mid] <= n:
                lo = mid + 1
            else:
                hi = mid
        return S[lo - 1]
