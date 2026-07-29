// LeetCode 1572 - Matrix Diagonal Sum
// https://leetcode.com/problems/matrix-diagonal-sum/

#include <vector>

class Solution {
public:
    int diagonalSum(std::vector<std::vector<int>>& mat) {
        const int n = static_cast<int>(mat.size());
        int total = 0;
        for (int i = 0; i < n; ++i) {
            total += mat[i][i] + mat[i][n - 1 - i];
        }
        if (n % 2) {
            total -= mat[n / 2][n / 2];
        }
        return total;
    }
};
