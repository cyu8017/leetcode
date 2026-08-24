# LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        mod = 1000000007
        n = len(nums)
        tree = [{"sum": 0, "sumSq": 0, "lazy": 0} for _ in range(4 * (n + 2))]

        def apply(idx: int, l: int, r: int, val: int) -> None:
            length = r - l + 1
            tree[idx]["sumSq"] = (
                tree[idx]["sumSq"]
                + 2 * val % mod * tree[idx]["sum"] % mod
                + val % mod * val % mod * length % mod
            ) % mod
            tree[idx]["sum"] = (tree[idx]["sum"] + val % mod * length % mod) % mod
            tree[idx]["lazy"] = (tree[idx]["lazy"] + val) % mod

        def update(idx: int, l: int, r: int, ql: int, qr: int, val: int) -> None:
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                apply(idx, l, r, val)
                return
            if tree[idx]["lazy"] != 0 and l != r:
                mid = (l + r) // 2
                apply(idx * 2, l, mid, tree[idx]["lazy"])
                apply(idx * 2 + 1, mid + 1, r, tree[idx]["lazy"])
                tree[idx]["lazy"] = 0
            mid = (l + r) // 2
            update(idx * 2, l, mid, ql, qr, val)
            update(idx * 2 + 1, mid + 1, r, ql, qr, val)
            tree[idx]["sum"] = (tree[idx * 2]["sum"] + tree[idx * 2 + 1]["sum"]) % mod
            tree[idx]["sumSq"] = (tree[idx * 2]["sumSq"] + tree[idx * 2 + 1]["sumSq"]) % mod

        last = {}
        ans = 0
        for i in range(1, n + 1):
            v = nums[i - 1]
            prev = last.get(v, 0)
            update(1, 1, n, prev + 1, i, 1)
            ans = (ans + tree[1]["sumSq"]) % mod
            last[v] = i
        return ans
