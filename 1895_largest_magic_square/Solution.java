// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

class Solution {
    public int largestMagicSquare(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int[][] rowPrefix = new int[rows][cols + 1];
        int[][] colPrefix = new int[cols][rows + 1];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                rowPrefix[i][j + 1] = rowPrefix[i][j] + grid[i][j];
                colPrefix[j][i + 1] = colPrefix[j][i] + grid[i][j];
            }
        }

        for (int size = Math.min(rows, cols); size >= 1; size--) {
            for (int rowStart = 0; rowStart <= rows - size; rowStart++) {
                for (int colStart = 0; colStart <= cols - size; colStart++) {
                    if (isMagic(grid, rowPrefix, colPrefix, rowStart, colStart, size)) {
                        return size;
                    }
                }
            }
        }
        return 1;
    }

    private boolean isMagic(
            int[][] grid,
            int[][] rowPrefix,
            int[][] colPrefix,
            int rowStart,
            int colStart,
            int size) {
        int target = rowSum(rowPrefix, rowStart, colStart, colStart + size - 1);
        for (int row = rowStart; row < rowStart + size; row++) {
            if (rowSum(rowPrefix, row, colStart, colStart + size - 1) != target) {
                return false;
            }
        }
        for (int col = colStart; col < colStart + size; col++) {
            if (colSum(colPrefix, col, rowStart, rowStart + size - 1) != target) {
                return false;
            }
        }
        int diag1 = 0;
        int diag2 = 0;
        for (int offset = 0; offset < size; offset++) {
            diag1 += grid[rowStart + offset][colStart + offset];
            diag2 += grid[rowStart + offset][colStart + size - 1 - offset];
        }
        return diag1 == target && diag2 == target;
    }

    private int rowSum(int[][] rowPrefix, int row, int colStart, int colEnd) {
        return rowPrefix[row][colEnd + 1] - rowPrefix[row][colStart];
    }

    private int colSum(int[][] colPrefix, int col, int rowStart, int rowEnd) {
        return colPrefix[col][rowEnd + 1] - colPrefix[col][rowStart];
    }
}
