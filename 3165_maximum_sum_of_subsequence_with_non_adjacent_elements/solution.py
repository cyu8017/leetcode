# LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
# https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

from typing import List


class Node:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.s00 = 0
        self.s01 = 0
        self.s10 = 0
        self.s11 = 0


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        tr = [Node() for _ in range(n * 4)]

        def build(u: int, l: int, r: int) -> None:
            tr[u].l = l
            tr[u].r = r
            if l == r:
                return
            mid = (l + r) >> 1
            build(u << 1, l, mid)
            build(u << 1 | 1, mid + 1, r)

        def pushup(u: int) -> None:
            left = tr[u << 1]
            right = tr[u << 1 | 1]
            tr[u].s00 = max(left.s00 + right.s10, left.s01 + right.s00)
            tr[u].s01 = max(left.s00 + right.s11, left.s01 + right.s01)
            tr[u].s10 = max(left.s10 + right.s10, left.s11 + right.s00)
            tr[u].s11 = max(left.s10 + right.s11, left.s11 + right.s01)

        def modify(u: int, x: int, v: int) -> None:
            if tr[u].l == tr[u].r:
                tr[u].s11 = max(0, v)
                return
            mid = (tr[u].l + tr[u].r) >> 1
            if x <= mid:
                modify(u << 1, x, v)
            else:
                modify(u << 1 | 1, x, v)
            pushup(u)

        def query(u: int, l: int, r: int) -> int:
            if tr[u].l >= l and tr[u].r <= r:
                return tr[u].s11
            mid = (tr[u].l + tr[u].r) >> 1
            ans = 0
            if r <= mid:
                ans = query(u << 1, l, r)
            if l > mid:
                ans = max(ans, query(u << 1 | 1, l, r))
            return ans

        build(1, 1, n)
        for i in range(n):
            modify(1, i + 1, nums[i])
        MOD = 1000000007
        ans = 0
        for q in queries:
            modify(1, q[0] + 1, q[1])
            ans = (ans + query(1, 1, n)) % MOD
        return ans
