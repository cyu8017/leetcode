// LeetCode 0240 - Search a 2D Matrix II
// https://leetcode.com/problems/search-a-2d-matrix-ii/

#include <vector>

class Solution {
public:
    bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) {
            return false;
        }
        int row = 0;
        int col = static_cast<int>(matrix[0].size()) - 1;
        while (row < static_cast<int>(matrix.size()) && col >= 0) {
            int value = matrix[row][col];
            if (value == target) {
                return true;
            }
            if (value > target) {
                col--;
            } else {
                row++;
            }
        }
        return false;
    }
};
