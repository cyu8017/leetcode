// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution {
    public int countSquares(int[][] matrix) {
        int answer = 0;
        for (int r = 0; r < matrix.length; r++) {
            for (int c = 0; c < matrix[0].length; c++) {
                if (matrix[r][c] != 0 && r > 0 && c > 0) {
                    matrix[r][c] += Math.min(
                        matrix[r - 1][c],
                        Math.min(matrix[r][c - 1], matrix[r - 1][c - 1]));
                }
                answer += matrix[r][c];
            }
        }
        return answer;
    }
}
