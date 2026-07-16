// LeetCode 0498 - Diagonal Traverse
// https://leetcode.com/problems/diagonal-traverse/

public class Solution {
    public int[] FindDiagonalOrder(int[][] mat) {
        if (mat.Length == 0 || mat[0].Length == 0) {
            return Array.Empty<int>();
        }
        int rows = mat.Length;
        int cols = mat[0].Length;
        int[] result = new int[rows * cols];
        int row = 0;
        int col = 0;
        bool upward = true;
        int index = 0;

        while (index < rows * cols) {
            result[index++] = mat[row][col];
            if (upward) {
                if (col == cols - 1) {
                    row++;
                    upward = false;
                } else if (row == 0) {
                    col++;
                    upward = false;
                } else {
                    row--;
                    col++;
                }
            } else {
                if (row == rows - 1) {
                    col++;
                    upward = true;
                } else if (col == 0) {
                    row++;
                    upward = true;
                } else {
                    row++;
                    col--;
                }
            }
        }
        return result;
    }
}
