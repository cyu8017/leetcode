# LeetCode 2709 - Greatest Common Divisor Traversal
# https://leetcode.com/problems/greatest-common-divisor-traversal/

from typing import List


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        mx = nums[0]
        for x in nums:
            if x > mx:
                mx = x
        parent = list(range(mx + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        has = [False] * (mx + 1)
        for x in nums:
            if x == 1:
                return False
            has[x] = True
        sieve = [0] * (mx + 1)
        for i in range(2, mx + 1):
            if sieve[i] == 0:
                for j in range(i, mx + 1, i):
                    if sieve[j] == 0:
                        sieve[j] = i
                    if has[j]:
                        unite(i, j)
        root = find(nums[0])
        for x in nums:
            if find(x) != root:
                return False
        return True
