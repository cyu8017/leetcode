// LeetCode 0861 - Score After Flipping Matrix
// https://leetcode.com/problems/score-after-flipping-matrix/

#include <algorithm>
#include <vector>

class Solution {
public:
    int matrixScore(std::vector<std::vector<int>>& grid) {
        int m = static_cast<int>(grid.size());
        int n = static_cast<int>(grid[0].size());
        for (auto& row : grid) {
            if (row[0] == 0) {
                for (int j = 0; j < n; ++j) {
                    row[j] ^= 1;
                }
            }
        }
        int ans = m * (1 << (n - 1));
        for (int j = 1; j < n; ++j) {
            int ones = 0;
            for (int i = 0; i < m; ++i) {
                ones += grid[i][j];
            }
            ans += std::max(ones, m - ones) * (1 << (n - 1 - j));
        }
        return ans;
    }
};
