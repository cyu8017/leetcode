// LeetCode 3665 - Twisted Mirror Path Count
// https://leetcode.com/problems/twisted-mirror-path-count/

#include <vector>

class Solution {
public:
    int uniquePaths(std::vector<std::vector<int>>& grid) {
        const int MOD = 1000000007;
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> dp(m, std::vector<int>(n));
        if (grid[0][0] == 1) return 0;
        dp[0][0] = 1;
        auto nextCell = [&](int i, int j, int di, int dj) -> std::tuple<int, int, bool> {
            int ni = i + di, nj = j + dj;
            while (ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1) {
                if (dj == 1) {
                    di = 1;
                    dj = 0;
                } else {
                    di = 0;
                    dj = 1;
                }
                ni += di;
                nj += dj;
            }
            if (ni < 0 || nj < 0 || ni >= m || nj >= n) return {0, 0, false};
            return {ni, nj, true};
        };
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 || dp[i][j] == 0) continue;
                auto [ni, nj, ok] = nextCell(i, j, 0, 1);
                if (ok) dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD;
                auto [ni2, nj2, ok2] = nextCell(i, j, 1, 0);
                if (ok2) dp[ni2][nj2] = (dp[ni2][nj2] + dp[i][j]) % MOD;
            }
        }
        return dp[m - 1][n - 1];
    }
};
