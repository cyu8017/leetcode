# LeetCode 3378 - Count Connected Components in LCM Graph
# https://leetcode.com/problems/count-connected-components-in-lcm-graph/

from typing import List


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        idx = {}
        for i, v in enumerate(nums):
            idx[v] = i
        for d in range(1, threshold + 1):
            first = -1
            for m in range(d, threshold + 1, d):
                if m in idx:
                    i = idx[m]
                    if first == -1:
                        first = i
                    elif nums[first] * nums[i] // gcd(nums[first], nums[i]) <= threshold:
                        unite(first, i)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = nums[i], nums[j]
                g = gcd(a, b)
                if (a // g) * b <= threshold:
                    unite(i, j)
        return len({find(i) for i in range(n)})
