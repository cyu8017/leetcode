# LeetCode 3399 - Smallest Substring With Identical Characters II
# https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/


class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        def ok(L: int) -> bool:
            ops = 0
            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                ops += (j - i) // (L + 1)
                i = j
            return ops <= numOps

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
