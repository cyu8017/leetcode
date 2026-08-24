# LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/


class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        ans = -10**9
        for a in range(5):
            for b in range(5):
                if a == b:
                    continue
                pref_a = [0] * (n + 1)
                pref_b = [0] * (n + 1)
                for i in range(n):
                    pref_a[i + 1] = pref_a[i]
                    pref_b[i + 1] = pref_b[i]
                    if ord(s[i]) - 48 == a:
                        pref_a[i + 1] += 1
                    if ord(s[i]) - 48 == b:
                        pref_b[i + 1] += 1
                for i in range(n):
                    for j in range(i + k - 1, n):
                        fa = pref_a[j + 1] - pref_a[i]
                        fb = pref_b[j + 1] - pref_b[i]
                        if fa % 2 == 1 and fb % 2 == 0 and fb > 0:
                            if fa - fb > ans:
                                ans = fa - fb
        return ans
