# LeetCode 2746 - Decremental String Concatenation
# https://leetcode.com/problems/decremental-string-concatenation/

from typing import List


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        memo = {}
        w0 = words[0]

        def dfs(i: int, first: str, last: str) -> int:
            if i == n:
                return 0
            key = (i, first, last)
            if key in memo:
                return memo[key]
            w = words[i]
            wf, wl = w[0], w[-1]
            add1 = len(w) - (1 if last == wf else 0)
            add2 = len(w) - (1 if wl == first else 0)
            a = add1 + dfs(i + 1, first, wl)
            b = add2 + dfs(i + 1, wf, last)
            ans = min(a, b)
            memo[key] = ans
            return ans

        return len(w0) + dfs(1, w0[0], w0[-1])
