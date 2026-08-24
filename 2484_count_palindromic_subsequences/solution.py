# LeetCode 2484 - Count Palindromic Subsequences
# https://leetcode.com/problems/count-palindromic-subsequences/


class Solution:
    def countPalindromes(self, s: str) -> int:
        mod = 1000000007
        n = len(s)
        pref = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        suf = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        cnt = [0] * 10
        for i in range(n):
            if i > 0:
                for a in range(10):
                    for b in range(10):
                        pref[i][a][b] = pref[i - 1][a][b]
            d = ord(s[i]) - 48
            for a in range(10):
                pref[i][a][d] += cnt[a]
            cnt[d] += 1
        cnt = [0] * 10
        for i in range(n - 1, -1, -1):
            if i + 1 < n:
                for a in range(10):
                    for b in range(10):
                        suf[i][a][b] = suf[i + 1][a][b]
            d = ord(s[i]) - 48
            for a in range(10):
                suf[i][a][d] += cnt[a]
            cnt[d] += 1
        ans = 0
        for i in range(2, n - 2):
            for a in range(10):
                for b in range(10):
                    ans = (ans + pref[i - 1][a][b] * suf[i + 1][a][b]) % mod
        return ans
