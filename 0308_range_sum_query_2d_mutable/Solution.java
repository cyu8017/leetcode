// LeetCode 0308 - Range Sum Query 2D - Mutable
// https://leetcode.com/problems/range-sum-query-2d-mutable/

class NumMatrix {
    private final int[][] matrix;
    private final int[][] tree;
    private final int rows;
    private final int cols;

    public NumMatrix(int[][] matrix) {
        this.rows = matrix.length;
        this.cols = rows == 0 ? 0 : matrix[0].length;
        this.matrix = new int[rows][cols];
        this.tree = new int[rows + 1][cols + 1];
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                this.matrix[row][col] = matrix[row][col];
                add(row + 1, col + 1, matrix[row][col]);
            }
        }
    }

    public void update(int row, int col, int val) {
        int delta = val - matrix[row][col];
        matrix[row][col] = val;
        add(row + 1, col + 1, delta);
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        return prefix(row2 + 1, col2 + 1)
                - prefix(row1, col2 + 1)
                - prefix(row2 + 1, col1)
                + prefix(row1, col1);
    }

    private void add(int row, int col, int delta) {
        int rowIndex = row;
        while (rowIndex <= rows) {
            int colIndex = col;
            while (colIndex <= cols) {
                tree[rowIndex][colIndex] += delta;
                colIndex += colIndex & -colIndex;
            }
            rowIndex += rowIndex & -rowIndex;
        }
    }

    private int prefix(int row, int col) {
        int total = 0;
        int rowIndex = row;
        while (rowIndex > 0) {
            int colIndex = col;
            while (colIndex > 0) {
                total += tree[rowIndex][colIndex];
                colIndex -= colIndex & -colIndex;
            }
            rowIndex -= rowIndex & -rowIndex;
        }
        return total;
    }
}
