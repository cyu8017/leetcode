// LeetCode 0308 - Range Sum Query 2D - Mutable
// https://leetcode.com/problems/range-sum-query-2d-mutable/

#include <vector>

class NumMatrix {
    std::vector<std::vector<int>> matrix;
    std::vector<std::vector<int>> tree;
    int rows;
    int cols;

    void add(int row, int col, int delta) {
        for (int rowIndex = row; rowIndex <= rows; rowIndex += rowIndex & -rowIndex) {
            for (int colIndex = col; colIndex <= cols; colIndex += colIndex & -colIndex) {
                tree[rowIndex][colIndex] += delta;
            }
        }
    }

    int prefix(int row, int col) const {
        int total = 0;
        for (int rowIndex = row; rowIndex > 0; rowIndex -= rowIndex & -rowIndex) {
            for (int colIndex = col; colIndex > 0; colIndex -= colIndex & -colIndex) {
                total += tree[rowIndex][colIndex];
            }
        }
        return total;
    }

public:
    NumMatrix(std::vector<std::vector<int>>& matrix)
        : matrix(matrix),
          rows(static_cast<int>(matrix.size())),
          cols(rows ? static_cast<int>(matrix[0].size()) : 0),
          tree(rows + 1, std::vector<int>(cols + 1, 0)) {
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                add(row + 1, col + 1, matrix[row][col]);
            }
        }
    }

    void update(int row, int col, int val) {
        int delta = val - matrix[row][col];
        matrix[row][col] = val;
        add(row + 1, col + 1, delta);
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        return prefix(row2 + 1, col2 + 1) - prefix(row1, col2 + 1) - prefix(row2 + 1, col1)
            + prefix(row1, col1);
    }
};
