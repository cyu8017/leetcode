# LeetCode 2272 - Substring With Largest Variance
# https://leetcode.com/problems/substring-with-largest-variance/


class Solution:
    def largestVariance(self, s: str) -> int:
        ans = 0
        for ai in range(26):
            for bi in range(26):
                if ai == bi:
                    continue
                a = chr(97 + ai)
                b = chr(97 + bi)
                bal = 0
                has_b = False
                for c in s:
                    if c == a:
                        bal += 1
                    elif c == b:
                        bal -= 1
                        has_b = True
                    if has_b:
                        ans = max(ans, bal)
                    if bal < 0:
                        bal = 0
                        has_b = False
        return ans
