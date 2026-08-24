# LeetCode 3518 - Smallest Palindromic Rearrangement II
# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

from typing import List

MAX = 1000001


def nCk(n: int, kk: int) -> int:
    if kk < 0 or kk > n:
        return 0
    res = 1
    if kk > n - kk:
        kk = n - kk
    for i in range(1, kk + 1):
        res = res * (n - i + 1) // i
        if res >= MAX:
            return MAX
    return res


def countArr(h: List[int]) -> int:
    total = 0
    for f in h:
        total += f
    res = 1
    for f in h:
        res *= nCk(total, f)
        if res >= MAX:
            return MAX
        total -= f
    return res


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        odd = 0
        for c in cnt:
            if c % 2 != 0:
                odd += 1
        if odd > 1:
            return ""
        half = [0] * 26
        mid = ""
        for i in range(26):
            half[i] = cnt[i] // 2
            if cnt[i] % 2 != 0:
                mid = chr(97 + i)
        if countArr(half) < k:
            return ""
        half_len = 0
        for f in half:
            half_len += f
        left = ""
        for _ in range(half_len):
            for i in range(26):
                if half[i] == 0:
                    continue
                half[i] -= 1
                arr = countArr(half)
                if arr >= k:
                    left += chr(97 + i)
                    break
                k -= arr
                half[i] += 1
        res = left
        if mid:
            res += mid
        for i in range(len(left) - 1, -1, -1):
            res += left[i]
        return res
