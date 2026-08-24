# LeetCode 3898 - Find The Degree Of Each Vertex
# https://leetcode.com/problems/find-the-degree-of-each-vertex/

from typing import List


class Solution:
    def findDegrees(self, matrix: List[List[int]]) -> List[int]:
        ans = [0] * len(matrix)
        for i in range(len(matrix)):
            for x in matrix[i]:
                ans[i] += x
        return ans
