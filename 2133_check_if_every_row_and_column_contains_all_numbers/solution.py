# LeetCode 2133 - Check if Every Row and Column Contains All Numbers
# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

from typing import List
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            row = [False] * (n + 1)
            col = [False] * (n + 1)
            for j in range(n):
                if row[matrix[i][j]] or col[matrix[j][i]]:
                    return False
                row[matrix[i][j]] = col[matrix[j][i]] = True
        return True
