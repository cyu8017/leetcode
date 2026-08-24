# LeetCode 3044 - Most Frequent Prime
# https://leetcode.com/problems/most-frequent-prime/

from typing import List


def isPrime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i <= n // i:
        if n % i == 0:
            return False
        i += 1
    return True


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        cnt = {}
        for i in range(m):
            for j in range(n):
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if a == 0 and b == 0:
                            continue
                        x = i + a
                        y = j + b
                        v = mat[i][j]
                        while x >= 0 and x < m and y >= 0 and y < n:
                            v = v * 10 + mat[x][y]
                            if isPrime(v):
                                cnt[v] = cnt.get(v, 0) + 1
                            x += a
                            y += b
        ans = -1
        mx = 0
        for key, value in cnt.items():
            if mx < value or (mx == value and ans < key):
                mx = value
                ans = key
        return ans
