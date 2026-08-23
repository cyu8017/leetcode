// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

#include <algorithm>
#include <climits>
#include <map>
#include <vector>

class Solution {
public:
    int minCost(std::vector<std::vector<int>>& grid, int k) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        const int inf = INT_MAX / 4;
        std::vector<std::vector<std::vector<int>>> f(k + 1, std::vector<std::vector<int>>(m, std::vector<int>(n, inf)));
        f[0][0][0] = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i > 0) f[0][i][j] = std::min(f[0][i][j], f[0][i - 1][j] + grid[i][j]);
                if (j > 0) f[0][i][j] = std::min(f[0][i][j], f[0][i][j - 1] + grid[i][j]);
            }
        }
        std::map<int, std::vector<std::pair<int, int>>, std::greater<int>> g;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) g[grid[i][j]].push_back({i, j});
        for (int t = 1; t <= k; t++) {
            int mn = inf;
            for (auto& [key, pos] : g) {
                for (auto& [pi, pj] : pos) mn = std::min(mn, f[t - 1][pi][pj]);
                for (auto& [pi, pj] : pos) f[t][pi][pj] = mn;
            }
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (i > 0) f[t][i][j] = std::min(f[t][i][j], f[t][i - 1][j] + grid[i][j]);
                    if (j > 0) f[t][i][j] = std::min(f[t][i][j], f[t][i][j - 1] + grid[i][j]);
                }
            }
        }
        int ans = inf;
        for (int t = 0; t <= k; t++) ans = std::min(ans, f[t][m - 1][n - 1]);
        return ans;
    }
};
