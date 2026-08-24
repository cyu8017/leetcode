# LeetCode 3337 - Total Characters in String After Transformations II
# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

from typing import List


def matMul(a: List[List[int]], b: List[List[int]], mod: int) -> List[List[int]]:
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if a[i][k] == 0:
                continue
            for j in range(n):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j] % mod) % mod
    return c


def matPow(a: List[List[int]], e: int, mod: int) -> List[List[int]]:
    n = len(a)
    r = [[0] * n for _ in range(n)]
    for i in range(n):
        r[i][i] = 1
    while e > 0:
        if e & 1:
            r = matMul(r, a, mod)
        a = matMul(a, a, mod)
        e >>= 1
    return r


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 1000000007
        mat = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(1, nums[i] + 1):
                mat[i][(i + j) % 26] = 1
        mat = matPow(mat, t, mod)
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        ans = 0
        for i in range(26):
            for j in range(26):
                ans = (ans + cnt[i] * mat[i][j] % mod) % mod
        return ans
