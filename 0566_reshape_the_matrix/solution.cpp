// LeetCode 0566 - Reshape the Matrix
// https://leetcode.com/problems/reshape-the-matrix/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> matrixReshape(std::vector<std::vector<int>>& mat, int r, int c) {
        int rows = static_cast<int>(mat.size());
        int cols = static_cast<int>(mat[0].size());
        if (rows * cols != r * c) {
            return mat;
        }

        std::vector<std::vector<int>> result(r, std::vector<int>(c));
        int index = 0;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                result[i][j] = mat[index / cols][index % cols];
                ++index;
            }
        }
        return result;
    }
};
