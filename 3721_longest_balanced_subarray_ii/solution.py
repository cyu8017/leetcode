# LeetCode 3721 - Longest Balanced Subarray II
# https://leetcode.com/problems/longest-balanced-subarray-ii/

from typing import List


class Node:
    def __init__(self) -> None:
        self.l = 0
        self.r = 0
        self.mn = 0
        self.mx = 0
        self.lazy = 0


class SegmentTree:
    def __init__(self, n: int) -> None:
        self.tr = [Node() for _ in range(n << 2)]
        self.build(1, 0, n)

    def build(self, u: int, l: int, r: int) -> None:
        tr = self.tr
        tr[u].l = l
        tr[u].r = r
        tr[u].mn = 0
        tr[u].mx = 0
        tr[u].lazy = 0
        if l == r:
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)

    def apply(self, u: int, v: int) -> None:
        self.tr[u].mn += v
        self.tr[u].mx += v
        self.tr[u].lazy += v

    def pushup(self, u: int) -> None:
        tr = self.tr
        tr[u].mn = min(tr[u << 1].mn, tr[u << 1 | 1].mn)
        tr[u].mx = max(tr[u << 1].mx, tr[u << 1 | 1].mx)

    def pushdown(self, u: int) -> None:
        if self.tr[u].lazy != 0:
            v = self.tr[u].lazy
            self.apply(u << 1, v)
            self.apply(u << 1 | 1, v)
            self.tr[u].lazy = 0

    def modify(self, u: int, l: int, r: int, v: int) -> None:
        tr = self.tr
        if tr[u].l >= l and tr[u].r <= r:
            self.apply(u, v)
            return
        self.pushdown(u)
        mid = (tr[u].l + tr[u].r) >> 1
        if l <= mid:
            self.modify(u << 1, l, r, v)
        if r > mid:
            self.modify(u << 1 | 1, l, r, v)
        self.pushup(u)

    def query(self, u: int, target: int) -> int:
        tr = self.tr
        if tr[u].l == tr[u].r:
            return tr[u].l
        self.pushdown(u)
        left = u << 1
        right = u << 1 | 1
        if tr[left].mn <= target <= tr[left].mx:
            return self.query(left, target)
        return self.query(right, target)


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        st = SegmentTree(n)
        last = {}
        now = 0
        ans = 0
        for i in range(1, n + 1):
            x = nums[i - 1]
            det = 1 if (x & 1) != 0 else -1
            if x in last:
                st.modify(1, last[x], n, -det)
                now -= det
            last[x] = i
            st.modify(1, i, n, det)
            now += det
            pos = st.query(1, now)
            ans = max(ans, i - pos)
        return ans
