// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

public class Solution {
    public int LargestMagicSquare(int[][] grid) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        var rowPrefix = new int[rows][];
        var colPrefix = new int[cols][];
        for (int i = 0; i < rows; i++) {
            rowPrefix[i] = new int[cols + 1];
        }
        for (int j = 0; j < cols; j++) {
            colPrefix[j] = new int[rows + 1];
        }
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                rowPrefix[i][j + 1] = rowPrefix[i][j] + grid[i][j];
                colPrefix[j][i + 1] = colPrefix[j][i] + grid[i][j];
            }
        }

        int RowSum(int row, int colStart, int colEnd) =>
            rowPrefix[row][colEnd + 1] - rowPrefix[row][colStart];

        int ColSum(int col, int rowStart, int rowEnd) =>
            colPrefix[col][rowEnd + 1] - colPrefix[col][rowStart];

        bool IsMagic(int rowStart, int colStart, int size) {
            int target = RowSum(rowStart, colStart, colStart + size - 1);
            for (int row = rowStart; row < rowStart + size; row++) {
                if (RowSum(row, colStart, colStart + size - 1) != target) {
                    return false;
                }
            }
            for (int col = colStart; col < colStart + size; col++) {
                if (ColSum(col, rowStart, rowStart + size - 1) != target) {
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

        for (int size = Math.Min(rows, cols); size >= 1; size--) {
            for (int rowStart = 0; rowStart <= rows - size; rowStart++) {
                for (int colStart = 0; colStart <= cols - size; colStart++) {
                    if (IsMagic(rowStart, colStart, size)) {
                        return size;
                    }
                }
            }
        }
        return 1;
    }
}
