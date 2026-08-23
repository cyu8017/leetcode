// LeetCode 0498 - Diagonal Traverse
// https://leetcode.com/problems/diagonal-traverse/

#include <vector>

class Solution {
public:
    std::vector<int> findDiagonalOrder(std::vector<std::vector<int>>& mat) {
        if (mat.empty() || mat[0].empty()) {
            return {};
        }
        const int rows = static_cast<int>(mat.size());
        const int cols = static_cast<int>(mat[0].size());
        std::vector<int> result;
        result.reserve(rows * cols);
        int row = 0;
        int col = 0;
        bool upward = true;

        for (int count = 0; count < rows * cols; ++count) {
            result.push_back(mat[row][col]);
            if (upward) {
                if (col == cols - 1) {
                    ++row;
                    upward = false;
                } else if (row == 0) {
                    ++col;
                    upward = false;
                } else {
                    --row;
                    ++col;
                }
            } else {
                if (row == rows - 1) {
                    ++col;
                    upward = true;
                } else if (col == 0) {
                    ++row;
                    upward = true;
                } else {
                    ++row;
                    --col;
                }
            }
        }
        return result;
    }
};
