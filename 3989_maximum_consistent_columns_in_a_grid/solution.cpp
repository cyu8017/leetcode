// LeetCode 3989 - Maximum Consistent Columns in a Grid
// https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/

#include <cstdlib>
#include <vector>

class Solution {
public:
    int maxConsistentColumns(std::vector<std::vector<int>>& grid, int limit) {
        int m = (int)grid.size();
        int n = (int)grid[0].size();
        std::vector<int> dp(n, 1);
        int ans = 1;
        for (int j = 0; j < n; j++) {
            dp[j] = 1;
            for (int i = 0; i < j; i++) {
                if (dp[i] + 1 <= dp[j]) continue;
                bool ok = true;
                for (int r = 0; r < m; r++) {
                    int d = std::abs(grid[r][j] - grid[r][i]);
                    if (d > limit) {
                        ok = false;
                        break;
                    }
                }
                if (ok) dp[j] = dp[i] + 1;
            }
            if (dp[j] > ans) ans = dp[j];
        }
        return ans;
    }
};
