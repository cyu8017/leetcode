// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

#include <array>
#include <vector>

class Solution {
public:
    int minXor(std::vector<std::vector<int>>& grid) {
        int rows = (int)grid.size(), cols = (int)grid[0].size();
        std::vector<std::array<bool, 1024>> dp(cols);
        for (int row = 0; row < rows; row++) {
            std::array<bool, 1024> left{};
            for (int col = 0; col < cols; col++) {
                std::array<bool, 1024> next{};
                int value = grid[row][col];
                if (row == 0 && col == 0) {
                    next[value] = true;
                } else {
                    for (int xorv = 0; xorv < 1024; xorv++) {
                        if (dp[col][xorv] || left[xorv]) next[xorv ^ value] = true;
                    }
                }
                dp[col] = next;
                left = next;
            }
        }
        for (int xorv = 0; xorv < 1024; xorv++) {
            if (dp[cols - 1][xorv]) return xorv;
        }
        return -1;
    }
};
