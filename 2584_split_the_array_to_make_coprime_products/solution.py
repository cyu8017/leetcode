# LeetCode 2584 - Split the Array to Make Coprime Products
# https://leetcode.com/problems/split-the-array-to-make-coprime-products/

from typing import List


class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        first = {}
        last = {}

        def factorize(x: int, idx: int) -> None:
            p = 2
            while p * p <= x:
                if x % p == 0:
                    if p not in first:
                        first[p] = idx
                    last[p] = idx
                    while x % p == 0:
                        x //= p
                p += 1
            if x > 1:
                if x not in first:
                    first[x] = idx
                last[x] = idx

        n = len(nums)
        for i, num in enumerate(nums):
            factorize(num, i)
        far = 0
        for i in range(n - 1):
            x = nums[i]
            p = 2
            while p * p <= x:
                if x % p == 0:
                    if last[p] > far:
                        far = last[p]
                    while x % p == 0:
                        x //= p
                p += 1
            if x > 1 and last[x] > far:
                far = last[x]
            if far == i:
                return i
        return -1
