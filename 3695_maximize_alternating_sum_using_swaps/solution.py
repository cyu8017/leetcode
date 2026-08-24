# LeetCode 3695 - Maximize Alternating Sum Using Swaps
# https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in swaps:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
        comp_vals = {}
        comp_idx = {}
        for i in range(n):
            r = find(i)
            comp_vals.setdefault(r, []).append(nums[i])
            comp_idx.setdefault(r, []).append(i)
        arr = [0] * n
        for r, vals in comp_vals.items():
            idxs = comp_idx[r]
            vals.sort(reverse=True)
            even = sorted(i for i in idxs if i % 2 == 0)
            odd = sorted(i for i in idxs if i % 2 == 1)
            ei = 0
            for v in vals:
                if ei < len(even):
                    arr[even[ei]] = v
                else:
                    arr[odd[ei - len(even)]] = v
                ei += 1
        ans = 0
        for i in range(n):
            if i % 2 == 0:
                ans += arr[i]
            else:
                ans -= arr[i]
        return ans
