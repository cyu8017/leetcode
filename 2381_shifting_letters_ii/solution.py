# LeetCode 2381 - Shifting Letters II
# https://leetcode.com/problems/shifting-letters-ii/

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        for sh in shifts:
            d = -1 if sh[2] == 0 else 1
            diff[sh[0]] += d
            diff[sh[1] + 1] -= d
        arr = list(s)
        cur = 0
        for i in range(n):
            cur = (cur + diff[i]) % 26
            if cur < 0:
                cur += 26
            arr[i] = chr(97 + (ord(arr[i]) - 97 + cur) % 26)
        return "".join(arr)
