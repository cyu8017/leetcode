# LeetCode 3187 - Peaks in Array
# https://leetcode.com/problems/peaks-in-array/

from typing import List


class BIT:
    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, delta: int) -> None:
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = BIT(n - 1)

        def update_peak(i: int, val: int) -> None:
            if i <= 0 or i >= n - 1:
                return
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                tree.update(i, val)

        for i in range(1, n - 1):
            update_peak(i, 1)
        ans = []
        for q in queries:
            if q[0] == 1:
                l, r = q[1] + 1, q[2] - 1
                t = 0
                if l <= r:
                    t = tree.query(r) - tree.query(l - 1)
                ans.append(t)
            else:
                idx, val = q[1], q[2]
                for i in range(idx - 1, idx + 2):
                    update_peak(i, -1)
                nums[idx] = val
                for i in range(idx - 1, idx + 2):
                    update_peak(i, 1)
        return ans
