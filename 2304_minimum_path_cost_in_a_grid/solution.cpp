// LeetCode 2304 - Minimum Path Cost in a Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/

#include <vector>
#include <climits>
#include <algorithm>

class Solution {
public:
    int minPathCost(std::vector<std::vector<int>>& grid, std::vector<std::vector<int>>& moveCost) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<int> dp = grid[0];
        for (int r = 0; r < m - 1; ++r) {
            std::vector<int> next(n, INT_MAX / 2);
            for (int c = 0; c < n; ++c) {
                int from = grid[r][c];
                for (int nc = 0; nc < n; ++nc)
                    next[nc] = std::min(next[nc], dp[c] + moveCost[from][nc] + grid[r + 1][nc]);
            }
            dp = std::move(next);
        }
        return *std::min_element(dp.begin(), dp.end());
    }
};
