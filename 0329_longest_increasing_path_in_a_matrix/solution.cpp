// LeetCode 0329 - Longest Increasing Path in a Matrix
// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

#include <algorithm>
#include <vector>

class Solution {
    int dfs(
        const std::vector<std::vector<int>>& matrix,
        std::vector<std::vector<int>>& memo,
        int row,
        int col
    ) {
        if (memo[row][col] != 0) {
            return memo[row][col];
        }
        int best = 1;
        static const int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (const int* direction : directions) {
            int nextRow = row + direction[0];
            int nextCol = col + direction[1];
            if (nextRow >= 0 && nextRow < static_cast<int>(matrix.size()) &&
                nextCol >= 0 && nextCol < static_cast<int>(matrix[0].size()) &&
                matrix[nextRow][nextCol] > matrix[row][col]) {
                best = std::max(best, 1 + dfs(matrix, memo, nextRow, nextCol));
            }
        }
        memo[row][col] = best;
        return best;
    }

public:
    int longestIncreasingPath(std::vector<std::vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return 0;
        }
        int rows = static_cast<int>(matrix.size());
        int cols = static_cast<int>(matrix[0].size());
        std::vector<std::vector<int>> memo(rows, std::vector<int>(cols, 0));
        int best = 0;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                best = std::max(best, dfs(matrix, memo, row, col));
            }
        }
        return best;
    }
};
