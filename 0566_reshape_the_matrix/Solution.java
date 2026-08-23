// LeetCode 0566 - Reshape the Matrix
// https://leetcode.com/problems/reshape-the-matrix/

class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int rows = mat.length;
        int cols = mat[0].length;
        if (rows * cols != r * c) {
            return mat;
        }

        int[][] result = new int[r][c];
        int index = 0;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                result[i][j] = mat[index / cols][index % cols];
                ++index;
            }
        }
        return result;
    }
}
