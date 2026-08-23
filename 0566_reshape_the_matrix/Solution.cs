// LeetCode 0566 - Reshape the Matrix
// https://leetcode.com/problems/reshape-the-matrix/

public class Solution {
    public int[][] MatrixReshape(int[][] mat, int r, int c) {
        int rows = mat.Length, cols = mat[0].Length;
        if (rows * cols != r * c) return mat;
        int[][] result = new int[r][];
        for (int i = 0; i < r; ++i) result[i] = new int[c];
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
