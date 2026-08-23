// LeetCode 0766 - Toeplitz Matrix
// https://leetcode.com/problems/toeplitz-matrix/

public class Solution {
    public bool IsToeplitzMatrix(int[][] matrix) {
        for (int r = 1; r < matrix.Length; r++) {
            for (int c = 1; c < matrix[0].Length; c++) {
                if (matrix[r][c] != matrix[r - 1][c - 1]) return false;
            }
        }
        return true;
    }
}
