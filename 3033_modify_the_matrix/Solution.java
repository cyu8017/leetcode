// LeetCode 3033 - Modify the Matrix
// https://leetcode.com/problems/modify-the-matrix/

class Solution {
    public int[][] modifiedMatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        for (int j = 0; j < n; j++) {
            int mx = -1;
            for (int i = 0; i < m; i++) mx = Math.max(mx, matrix[i][j]);
            for (int i = 0; i < m; i++) if (matrix[i][j] == -1) matrix[i][j] = mx;
        }
        return matrix;
    }
}
