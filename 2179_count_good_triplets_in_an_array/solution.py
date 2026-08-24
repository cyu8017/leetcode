# LeetCode 2179 - Count Good Triplets in an Array
# https://leetcode.com/problems/count-good-triplets-in-an-array/

from typing import List


class Fenwick:
    def __init__(self, sz: int):
        self.bit = [0] * sz

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
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = [0] * n
        for i in range(n):
            pos2[nums2[i]] = i
        mapped = [0] * n
        for i in range(n):
            mapped[i] = pos2[nums1[i]]
        left = [0] * n
        right = [0] * n

        def makeFenwick(sz: int) -> Fenwick:
            return Fenwick(sz)

        fw = makeFenwick(n + 2)
        for i in range(n):
            left[i] = fw.sum(mapped[i])
            fw.add(mapped[i] + 1, 1)
        fw = makeFenwick(n + 2)
        for i in range(n - 1, -1, -1):
            right[i] = fw.sum(n) - fw.sum(mapped[i] + 1)
            fw.add(mapped[i] + 1, 1)
        ans = 0
        for i in range(n):
            ans += left[i] * right[i]
        return ans
