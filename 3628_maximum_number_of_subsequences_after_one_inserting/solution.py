# LeetCode 3628 - Maximum Number of Subsequences After One Inserting
# https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/


class Solution:
    def numOfSubsequences(self, s: str) -> int:
        def calc(st: str, t: str) -> int:
            cnt = 0
            a = 0
            for c in st:
                if c == t[1]:
                    cnt += a
                if c == t[0]:
                    a += 1
            return cnt

        l = r = 0
        for c in s:
            if c == "T":
                r += 1
        ans = 0
        mx = 0
        for c in s:
            if c == "T":
                r -= 1
            if c == "C":
                ans += l * r
            if c == "L":
                l += 1
            mx = max(mx, l * r)
        mx = max(mx, max(calc(s, "LC"), calc(s, "CT")))
        return ans + mx
