# LeetCode 0952 - Largest Component Size by Common Factor
# https://leetcode.com/problems/largest-component-size-by-common-factor/

from collections import Counter


class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        parent = list(range(max(nums) + 1))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            parent[find(a)] = find(b)

        def factors(x: int) -> list[int]:
            res = []
            d = 2
            while d * d <= x:
                if x % d == 0:
                    res.append(d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                res.append(x)
            return res

        for num in nums:
            for f in factors(num):
                union(num, f)

        return max(Counter(find(num) for num in nums).values())
