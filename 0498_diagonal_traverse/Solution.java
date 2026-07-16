// LeetCode 0498 - Diagonal Traverse
// https://leetcode.com/problems/diagonal-traverse/

class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        if (mat.length == 0 || mat[0].length == 0) {
            return new int[0];
        }
        int rows = mat.length;
        int cols = mat[0].length;
        int[] result = new int[rows * cols];
        int row = 0;
        int col = 0;
        boolean upward = true;
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
