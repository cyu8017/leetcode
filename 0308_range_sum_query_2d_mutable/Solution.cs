// LeetCode 0308 - Range Sum Query 2D - Mutable
// https://leetcode.com/problems/range-sum-query-2d-mutable/

public class NumMatrix {
    private readonly int[][] matrix;
    private readonly int[][] tree;
    private readonly int rows;
    private readonly int cols;

    public NumMatrix(int[][] matrix) {
        rows = matrix.Length;
        cols = rows == 0 ? 0 : matrix[0].Length;
        this.matrix = new int[rows][];
        tree = new int[rows + 1][];
        for (int row = 0; row < rows; row++) {
            this.matrix[row] = (int[])matrix[row].Clone();
        }
        for (int row = 0; row <= rows; row++) {
            tree[row] = new int[cols + 1];
        }
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                Add(row + 1, col + 1, matrix[row][col]);
            }
        }
    }

    public void Update(int row, int col, int val) {
        int delta = val - matrix[row][col];
        matrix[row][col] = val;
        Add(row + 1, col + 1, delta);
    }

    public int SumRegion(int row1, int col1, int row2, int col2) {
        return Prefix(row2 + 1, col2 + 1)
            - Prefix(row1, col2 + 1)
            - Prefix(row2 + 1, col1)
            + Prefix(row1, col1);
    }

    private void Add(int row, int col, int delta) {
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

    private int Prefix(int row, int col) {
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
