# LeetCode 3999 - Minimum Number of String Groups Through Transformations
# https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

from typing import List


class Solution:
    def leastRotation(self, s: str) -> int:
        n = len(s)
        i, j, k = 0, 1, 0
        while i < n and j < n and k < n:
            a = s[(i + k) % n]
            b = s[(j + k) % n]
            if a == b:
                k += 1
            else:
                if a > b:
                    i += k + 1
                else:
                    j += k + 1
                if i == j:
                    j += 1
                k = 0
        return i if i < j else j

    def canonicalRotate(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        r = self.leastRotation(s)
        if r == 0:
            return s
        return s[r:] + s[:r]

    def minimumGroups(self, words: List[str]) -> int:
        keys = []
        for w in words:
            n = len(w)
            even = ""
            odd = ""
            for i in range(n):
                if i % 2 == 0:
                    even += w[i]
                else:
                    odd += w[i]
            keys.append(self.canonicalRotate(even) + "#" + self.canonicalRotate(odd))
        keys.sort()
        groups = 0
        for i in range(len(keys)):
            if i == 0 or keys[i] != keys[i - 1]:
                groups += 1
        return groups
