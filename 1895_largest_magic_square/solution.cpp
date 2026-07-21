// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

#include <algorithm>
#include <vector>

class Solution {
public:
    int largestMagicSquare(std::vector<std::vector<int>>& grid) {
        int rows = static_cast<int>(grid.size());
        int cols = static_cast<int>(grid[0].size());
        std::vector<std::vector<int>> rowPrefix(rows, std::vector<int>(cols + 1, 0));
        std::vector<std::vector<int>> colPrefix(cols, std::vector<int>(rows + 1, 0));
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                rowPrefix[i][j + 1] = rowPrefix[i][j] + grid[i][j];
                colPrefix[j][i + 1] = colPrefix[j][i] + grid[i][j];
            }
        }

        auto rowSum = [&](int row, int colStart, int colEnd) {
            return rowPrefix[row][colEnd + 1] - rowPrefix[row][colStart];
        };
        auto colSum = [&](int col, int rowStart, int rowEnd) {
            return colPrefix[col][rowEnd + 1] - colPrefix[col][rowStart];
        };
        auto isMagic = [&](int rowStart, int colStart, int size) {
            int target = rowSum(rowStart, colStart, colStart + size - 1);
            for (int row = rowStart; row < rowStart + size; row++) {
                if (rowSum(row, colStart, colStart + size - 1) != target) return false;
            }
            for (int col = colStart; col < colStart + size; col++) {
                if (colSum(col, rowStart, rowStart + size - 1) != target) return false;
            }
            int diag1 = 0;
            int diag2 = 0;
            for (int offset = 0; offset < size; offset++) {
                diag1 += grid[rowStart + offset][colStart + offset];
                diag2 += grid[rowStart + offset][colStart + size - 1 - offset];
            }
            return diag1 == target && diag2 == target;
        };

        for (int size = std::min(rows, cols); size >= 1; size--) {
            for (int rowStart = 0; rowStart <= rows - size; rowStart++) {
                for (int colStart = 0; colStart <= cols - size; colStart++) {
                    if (isMagic(rowStart, colStart, size)) {
                        return size;
                    }
                }
            }
        }
        return 1;
    }
};
