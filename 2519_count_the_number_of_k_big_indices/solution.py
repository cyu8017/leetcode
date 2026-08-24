# LeetCode 2519 - Count the Number of K-Big Indices
# https://leetcode.com/problems/count-the-number-of-k-big-indices/

from typing import List


class Fenwick:
    def __init__(self, n: int):
        self.bit = [0] * (n + 2)

    def add(self, i: int, v: int) -> None:
        while i < len(self.bit):
            self.bit[i] += v
            i += i & -i

    def sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        uniq = sorted(nums)
        m = 0
        for i in range(len(uniq)):
            if i == 0 or uniq[i] != uniq[i - 1]:
                uniq[m] = uniq[i]
                m += 1
        rank = {uniq[i]: i + 1 for i in range(m)}
        left = [0] * n
        right = [0] * n
        ft = Fenwick(m)
        for i in range(n):
            r = rank[nums[i]]
            left[i] = ft.sum(r - 1)
            ft.add(r, 1)
        ft = Fenwick(m)
        for i in range(n - 1, -1, -1):
            r = rank[nums[i]]
            right[i] = ft.sum(r - 1)
            ft.add(r, 1)
        ans = 0
        for i in range(n):
            if left[i] >= k and right[i] >= k:
                ans += 1
        return ans
