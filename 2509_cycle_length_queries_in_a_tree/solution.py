# LeetCode 2509 - Cycle Length Queries in a Tree
# https://leetcode.com/problems/cycle-length-queries-in-a-tree/

from typing import List


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        for i in range(len(queries)):
            a, b = queries[i][0], queries[i][1]
            steps = 0
            while a != b:
                if a > b:
                    a //= 2
                else:
                    b //= 2
                steps += 1
            ans[i] = steps + 1
        return ans
