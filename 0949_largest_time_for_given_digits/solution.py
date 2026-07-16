# LeetCode 0949 - Largest Time for Given Digits
# https://leetcode.com/problems/largest-time-for-given-digits/

from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        best = ""
        for a, b, c, d in permutations(arr):
            hours, minutes = 10 * a + b, 10 * c + d
            if hours < 24 and minutes < 60:
                cand = f"{hours:02d}:{minutes:02d}"
                if cand > best:
                    best = cand
        return best
