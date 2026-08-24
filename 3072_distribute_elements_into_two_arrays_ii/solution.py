# LeetCode 3072 - Distribute Elements Into Two Arrays II
# https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

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
    def resultArray(self, nums: List[int]) -> List[int]:
        st = sorted(nums[:])
        n = len(st)
        tree1 = BIT(n + 1)
        tree2 = BIT(n + 1)

        def idx(x: int) -> int:
            lo = 0
            hi = len(st)
            while lo < hi:
                mid = (lo + hi) // 2
                if st[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo + 1

        arr1 = [nums[0]]
        arr2 = [nums[1]]
        tree1.update(idx(nums[0]), 1)
        tree2.update(idx(nums[1]), 1)
        for i in range(2, len(nums)):
            x = nums[i]
            id_ = idx(x)
            a = len(arr1) - tree1.query(id_)
            b = len(arr2) - tree2.query(id_)
            if a > b or (a == b and len(arr1) <= len(arr2)):
                arr1.append(x)
                tree1.update(id_, 1)
            else:
                arr2.append(x)
                tree2.update(id_, 1)
        return arr1 + arr2
