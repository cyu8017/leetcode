# LeetCode 3377 - Digit Operations to Make Two Integers Equal
# https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

from typing import List


def sieve(n: int) -> List[bool]:
    is_p = [False] * n
    for i in range(2, n):
        is_p[i] = True
    i = 2
    while i * i < n:
        if is_p[i]:
            for j in range(i * i, n, i):
                is_p[j] = False
        i += 1
    return is_p


class Solution:
    def minOperations(self, n: int, m: int) -> int:
        is_prime = sieve(100000)
        if is_prime[n]:
            return -1
        dist = [-1] * 100000
        pq = [[n, n]]
        dist[n] = n
        while pq:
            pq.sort(key=lambda a: a[0])
            cost, val = pq.pop(0)
            if cost != dist[val]:
                continue
            if val == m:
                return cost
            s = list(str(val))
            for i in range(len(s)):
                orig = s[i]
                for d in (-1, 1):
                    nd = (ord(orig) - 48) + d
                    if nd < 0 or nd > 9:
                        continue
                    if i == 0 and nd == 0 and len(s) > 1:
                        continue
                    s[i] = str(nd)
                    nv = int("".join(s), 10)
                    s[i] = orig
                    if is_prime[nv]:
                        continue
                    nc = cost + nv
                    if dist[nv] == -1 or nc < dist[nv]:
                        dist[nv] = nc
                        pq.append([nc, nv])
        return -1
