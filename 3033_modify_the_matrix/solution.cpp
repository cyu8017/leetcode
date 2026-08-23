// LeetCode 3033 - Modify the Matrix
// https://leetcode.com/problems/modify-the-matrix/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> modifiedMatrix(std::vector<std::vector<int>>& matrix) {
        int m = (int)matrix.size(), n = (int)matrix[0].size();
        for (int j = 0; j < n; j++) {
            int mx = -1;
            for (int i = 0; i < m; i++) mx = std::max(mx, matrix[i][j]);
            for (int i = 0; i < m; i++) if (matrix[i][j] == -1) matrix[i][j] = mx;
        }
        return matrix;
    }
};
