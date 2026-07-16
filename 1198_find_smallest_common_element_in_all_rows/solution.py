# LeetCode 1198 - Find Smallest Common Element in All Rows
# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        common = set(mat[0])
        for row in mat[1:]:
            common &= set(row)
            if not common:
                return -1
        return min(common)
