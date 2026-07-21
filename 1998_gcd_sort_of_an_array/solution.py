from typing import List

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        m = max(nums)
        parent = list(range(m + 1))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        # smallest prime factor
        spf = list(range(m + 1))
        for i in range(2, int(m**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, m + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        for x in set(nums):
            y = x
            while y > 1:
                p = spf[y]
                union(x, p)
                while y % p == 0:
                    y //= p

        sorted_nums = sorted(nums)
        for a, b in zip(nums, sorted_nums):
            if find(a) != find(b):
                return False
        return True
