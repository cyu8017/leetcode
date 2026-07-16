// LeetCode 0311 - Sparse Matrix Multiplication
// https://leetcode.com/problems/sparse-matrix-multiplication/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> multiply(
        std::vector<std::vector<int>>& mat1,
        std::vector<std::vector<int>>& mat2
    ) {
        int rows = static_cast<int>(mat1.size());
        int inner = static_cast<int>(mat1[0].size());
        int cols = static_cast<int>(mat2[0].size());
        std::vector<std::vector<int>> result(rows, std::vector<int>(cols, 0));

        for (int row = 0; row < rows; row++) {
            for (int index = 0; index < inner; index++) {
                if (mat1[row][index] == 0) {
                    continue;
                }
                for (int col = 0; col < cols; col++) {
                    if (mat2[index][col] != 0) {
                        result[row][col] += mat1[row][index] * mat2[index][col];
                    }
                }
            }
        }

        return result;
    }
};
