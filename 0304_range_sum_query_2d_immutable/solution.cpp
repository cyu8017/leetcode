// LeetCode 0304 - Range Sum Query 2D - Immutable
// https://leetcode.com/problems/range-sum-query-2d-immutable/

#include <vector>

class NumMatrix {
    std::vector<std::vector<int>> prefix;

public:
    NumMatrix(std::vector<std::vector<int>>& matrix) {
        int rows = static_cast<int>(matrix.size());
        int cols = rows ? static_cast<int>(matrix[0].size()) : 0;
        prefix.assign(rows + 1, std::vector<int>(cols + 1, 0));
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                prefix[row + 1][col + 1] = matrix[row][col]
                    + prefix[row][col + 1]
                    + prefix[row + 1][col]
                    - prefix[row][col];
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        int topLeft = prefix[row1][col1];
        int topRight = prefix[row1][col2 + 1];
        int bottomLeft = prefix[row2 + 1][col1];
        int bottomRight = prefix[row2 + 1][col2 + 1];
        return bottomRight - topRight - bottomLeft + topLeft;
    }
};
