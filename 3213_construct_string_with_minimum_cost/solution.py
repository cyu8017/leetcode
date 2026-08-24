# LeetCode 3213 - Construct String with Minimum Cost
# https://leetcode.com/problems/construct-string-with-minimum-cost/

from typing import List


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        bas, mod = 13331, 998244353
        inf = 10**18
        n = len(target)
        p = [0] * (n + 1)
        h = [0] * (n + 1)
        p[0] = 1
        h[0] = 0
        for i in range(1, n + 1):
            p[i] = (p[i - 1] * bas) % mod
            h[i] = (h[i - 1] * bas + ord(target[i - 1])) % mod

        def query(l: int, r: int) -> int:
            return (h[r] - (h[l - 1] * p[r - l + 1]) % mod + mod) % mod

        f = [inf] * (n + 1)
        f[0] = 0
        lengths = sorted({len(w) for w in words})
        d = {}
        for i in range(len(words)):
            x = 0
            for ch in words[i]:
                x = (x * bas + ord(ch)) % mod
            if x not in d or costs[i] < d[x]:
                d[x] = costs[i]
        for i in range(1, n + 1):
            for j in lengths:
                if j > i:
                    break
                x = query(i - j + 1, i)
                if x in d:
                    f[i] = min(f[i], f[i - j] + d[x])
        return -1 if f[n] >= inf else f[n]
