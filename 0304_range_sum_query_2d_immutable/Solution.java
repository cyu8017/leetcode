// LeetCode 0304 - Range Sum Query 2D - Immutable
// https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix {
    private final int[][] prefix;

    public NumMatrix(int[][] matrix) {
        int rows = matrix.length;
        int cols = rows == 0 ? 0 : matrix[0].length;
        prefix = new int[rows + 1][cols + 1];
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                prefix[row + 1][col + 1] = matrix[row][col]
                        + prefix[row][col + 1]
                        + prefix[row + 1][col]
                        - prefix[row][col];
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        int topLeft = prefix[row1][col1];
        int topRight = prefix[row1][col2 + 1];
        int bottomLeft = prefix[row2 + 1][col1];
        int bottomRight = prefix[row2 + 1][col2 + 1];
        return bottomRight - topRight - bottomLeft + topLeft;
    }
}
