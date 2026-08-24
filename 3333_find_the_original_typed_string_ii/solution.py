# LeetCode 3333 - Find the Original Typed String II
# https://leetcode.com/problems/find-the-original-typed-string-ii/


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 1000000007
        groups = []
        i = 0
        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i]:
                j += 1
            groups.append(j - i)
            i = j
        total = 1
        for g in groups:
            total = total * g % mod
        if k <= len(groups):
            return total
        need = k - 1
        dp = [0] * need
        dp[0] = 1
        for g in groups:
            ndp = [0] * need
            pref = [0] * (need + 1)
            for i in range(need):
                pref[i + 1] = (pref[i] + dp[i]) % mod
            for s in range(need):
                lo = s - g
                if lo < 0:
                    lo = 0
                hi = s - 1
                if hi >= 0:
                    ndp[s] = (pref[hi + 1] - pref[lo] + mod) % mod
            dp = ndp
        bad = 0
        for v in dp:
            bad = (bad + v) % mod
        return (total - bad + mod) % mod
