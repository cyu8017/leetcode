# LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
# https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

from typing import List


class Solution:
    def countNonAdjacentSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        mod = 1000000007
        n = len(parent)
        children: List[List[int]] = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        dp0: List[List[int]] = [None] * n
        dp1: List[List[int]] = [None] * n
        for u in range(n - 1, -1, -1):
            a = [0] * k
            b = [0] * k
            a[0] = 1
            b[(((nums[u] % k) + k) % k)] = 1
            for v in children[u]:
                na = [0] * k
                nb = [0] * k
                for x in range(k):
                    for y in range(k):
                        all_child = (dp0[v][y] + dp1[v][y]) % mod
                        na[(x + y) % k] = (na[(x + y) % k] + a[x] * all_child) % mod
                        nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v][y]) % mod
                a = na
                b = nb
            dp0[u] = a
            dp1[u] = b
        ans = (dp0[0][0] + dp1[0][0] - 1) % mod
        if ans < 0:
            ans += mod
        return ans
