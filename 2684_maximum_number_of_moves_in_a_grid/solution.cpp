// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maxMoves(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<int> dp(m, 0);
        for (int c = n - 2; c >= 0; c--) {
            std::vector<int> ndp(m, 0);
            for (int r = 0; r < m; r++) {
                int best = 0;
                for (int dr = -1; dr <= 1; dr++) {
                    int nr = r + dr;
                    if (nr >= 0 && nr < m && grid[nr][c + 1] > grid[r][c])
                        best = std::max(best, 1 + dp[nr]);
                }
                ndp[r] = best;
            }
            dp.swap(ndp);
        }
        return *std::max_element(dp.begin(), dp.end());
    }
};
