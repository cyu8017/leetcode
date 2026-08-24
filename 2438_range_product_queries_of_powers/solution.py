# LeetCode 2438 - Range Product Queries of Powers
# https://leetcode.com/problems/range-product-queries-of-powers/

from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 1000000007
        powers = []
        for bit in range(31):
            if ((n >> bit) & 1) != 0:
                powers.append(1 << bit)
        ans = [0] * len(queries)
        for i in range(len(queries)):
            prod = 1
            for j in range(queries[i][0], queries[i][1] + 1):
                prod = (prod * powers[j]) % mod
            ans[i] = prod
        return ans
