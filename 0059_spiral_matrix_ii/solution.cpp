// LeetCode 0059 - Spiral Matrix II
// https://leetcode.com/problems/spiral-matrix-ii/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> generateMatrix(int n) {
        std::vector<std::vector<int>> matrix(n, std::vector<int>(n, 0));
        int top = 0;
        int bottom = n - 1;
        int left = 0;
        int right = n - 1;
        int num = 1;

        while (top <= bottom && left <= right) {
            for (int col = left; col <= right; ++col) {
                matrix[top][col] = num++;
            }
            ++top;

            for (int row = top; row <= bottom; ++row) {
                matrix[row][right] = num++;
            }
            --right;

            if (top <= bottom) {
                for (int col = right; col >= left; --col) {
                    matrix[bottom][col] = num++;
                }
                --bottom;
            }

            if (left <= right) {
                for (int row = bottom; row >= top; --row) {
                    matrix[row][left] = num++;
                }
                ++left;
            }
        }

        return matrix;
    }
};
