# LeetCode 2213 - Longest Substring of One Repeating Character
# https://leetcode.com/problems/longest-substring-of-one-repeating-character/

from types import SimpleNamespace
from typing import List
class Solution:
    def longestRepeating(self, s_: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        def merge(a, b):
            if not a or a.size == 0:
                return b
            if not b or b.size == 0:
                return a
            res = SimpleNamespace(lChar=a.lChar, rChar=b.rChar, size=a.size + b.size, best=max(a.best, b.best), lLen=a.lLen, rLen=b.rLen)
            if a.rChar == b.lChar:
                mid = a.rLen + b.lLen
                res.best = max(res.best, mid)
                if a.lLen == a.size:
                    res.lLen = a.size + b.lLen
                if b.rLen == b.size:
                    res.rLen = b.size + a.rLen
            return res

        s = list(s_)
        n = len(s)
        tree = [None] * (4 * n + 5)
        def build(idx, l, r):
            if l == r:
                tree[idx] = SimpleNamespace(lChar=s[l], rChar=s[l], lLen=1, rLen=1, best=1, size=1)
                return
            mid = (l + r) >> 1
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)
            tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1])

        def update(idx, l, r, pos, ch):
            if l == r:
                s[pos] = ch
                tree[idx] = SimpleNamespace(lChar=ch, rChar=ch, lLen=1, rLen=1, best=1, size=1)
                return
            mid = (l + r) >> 1
            if pos <= mid:
                update(idx * 2, l, mid, pos, ch)
            else:
                update(idx * 2 + 1, mid + 1, r, pos, ch)
            tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1])

        build(1, 0, n - 1)
        ans = [None] * (len(queryIndices))
        for i in range(len(queryIndices)):
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i])
            ans[i] = tree[1].best
        return ans
