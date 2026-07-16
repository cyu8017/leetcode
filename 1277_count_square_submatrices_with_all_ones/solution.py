from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        answer = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] and r and c:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1])
                answer += matrix[r][c]
        return answer
