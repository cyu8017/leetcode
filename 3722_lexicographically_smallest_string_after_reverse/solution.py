# LeetCode 3722 - Lexicographically Smallest String After Reverse
# https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/


class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = s
        n = len(s)

        def reverse(a: list, l: int, r: int) -> None:
            i, j = l, r - 1
            while i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        for k in range(1, n + 1):
            a1 = list(s)
            reverse(a1, 0, k)
            t1 = "".join(a1)
            a2 = list(s)
            reverse(a2, n - k, n)
            t2 = "".join(a2)
            if t1 < ans:
                ans = t1
            if t2 < ans:
                ans = t2
        return ans
