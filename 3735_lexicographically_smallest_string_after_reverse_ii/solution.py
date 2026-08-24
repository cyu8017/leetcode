# LeetCode 3735 - Lexicographically Smallest String After Reverse II
# https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/


class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        best = s

        def reverse(a: list, l: int, r: int) -> None:
            i, j = l, r - 1
            while i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        for i in range(1, n + 1):
            t = list(s)
            reverse(t, 0, i)
            ts = "".join(t)
            if ts < best:
                best = ts
        for i in range(n):
            t = list(s)
            reverse(t, i, n)
            ts = "".join(t)
            if ts < best:
                best = ts
        return best
