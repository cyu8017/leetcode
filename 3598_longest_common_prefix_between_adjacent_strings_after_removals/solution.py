# LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
# https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

from typing import List


class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        tm = {}
        keys = []

        def calc(s: str, t: str) -> int:
            m = min(len(s), len(t))
            for k in range(m):
                if s[k] != t[k]:
                    return k
            return m

        def add_key(x: int) -> None:
            if x not in tm:
                tm[x] = 0
                lo, hi = 0, len(keys)
                while lo < hi:
                    mid = (lo + hi) >> 1
                    if keys[mid] < x:
                        lo = mid + 1
                    else:
                        hi = mid
                keys.insert(lo, x)
            tm[x] += 1

        def rem_key(x: int) -> None:
            c = tm[x] - 1
            if c == 0:
                del tm[x]
                ix = keys.index(x)
                if ix >= 0:
                    keys.pop(ix)
            else:
                tm[x] = c

        def add(i: int, j: int) -> None:
            if 0 <= i < n and 0 <= j < n:
                add_key(calc(words[i], words[j]))

        def remove(i: int, j: int) -> None:
            if 0 <= i < n and 0 <= j < n:
                rem_key(calc(words[i], words[j]))

        for i in range(n - 1):
            add(i, i + 1)
        ans = [0] * n
        for i in range(n):
            remove(i, i + 1)
            remove(i - 1, i)
            add(i - 1, i + 1)
            if keys and keys[-1] > 0:
                ans[i] = keys[-1]
            remove(i - 1, i + 1)
            add(i - 1, i)
            add(i, i + 1)
        return ans
