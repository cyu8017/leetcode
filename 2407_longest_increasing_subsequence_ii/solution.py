# LeetCode 2407 - Longest Increasing Subsequence II
# https://leetcode.com/problems/longest-increasing-subsequence-ii/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        max_v = 0
        for x in nums:
            max_v = max(max_v, x)
        tree = [0] * (4 * (max_v + 1))

        def update(idx: int, l: int, r: int, pos: int, val: int) -> None:
            if l == r:
                tree[idx] = max(tree[idx], val)
                return
            mid = (l + r) >> 1
            if pos <= mid:
                update(idx * 2, l, mid, pos, val)
            else:
                update(idx * 2 + 1, mid + 1, r, pos, val)
            tree[idx] = max(tree[idx * 2], tree[idx * 2 + 1])

        def query(idx: int, l: int, r: int, ql: int, qr: int) -> int:
            if qr < l or r < ql:
                return 0
            if ql <= l and r <= qr:
                return tree[idx]
            mid = (l + r) >> 1
            return max(query(idx * 2, l, mid, ql, qr), query(idx * 2 + 1, mid + 1, r, ql, qr))

        ans = 0
        for x in nums:
            lo = max(1, x - k)
            best = 1
            if lo <= x - 1:
                best = query(1, 1, max_v, lo, x - 1) + 1
            update(1, 1, max_v, x, best)
            ans = max(ans, best)
        return ans
