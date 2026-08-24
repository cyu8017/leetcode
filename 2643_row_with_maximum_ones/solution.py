# LeetCode 2643 - Row With Maximum Ones
# https://leetcode.com/problems/row-with-maximum-ones/

from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        best_row, best_cnt = 0, -1
        for i, row in enumerate(mat):
            cnt = sum(row)
            if cnt > best_cnt:
                best_cnt = cnt
                best_row = i
        return [best_row, best_cnt]
