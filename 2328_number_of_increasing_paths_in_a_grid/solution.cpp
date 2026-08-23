// LeetCode 2328 - Number of Increasing Paths in a Grid
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

#include <vector>
#include <functional>

class Solution {
public:
    int countPaths(std::vector<std::vector<int>>& grid) {
        const int mod = 1000000007;
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> dp(m, std::vector<int>(n));
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        std::function<int(int,int)> dfs = [&](int r, int c) {
            if (dp[r][c]) return dp[r][c];
            int res = 1;
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > grid[r][c])
                    res = (res + dfs(nr, nc)) % mod;
            }
            return dp[r][c] = res;
        };
        int ans = 0;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                ans = (ans + dfs(i, j)) % mod;
        return ans;
    }
};
