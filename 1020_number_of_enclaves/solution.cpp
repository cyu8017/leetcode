// LeetCode 1020 - Number of Enclaves
// https://leetcode.com/problems/number-of-enclaves/

#include <functional>
#include <vector>

class Solution {
public:
    int numEnclaves(std::vector<std::vector<int>>& grid) {
        int m = static_cast<int>(grid.size());
        int n = static_cast<int>(grid[0].size());
        std::function<void(int, int)> dfs = [&](int r, int c) {
            if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != 1) return;
            grid[r][c] = 0;
            dfs(r + 1, c);
            dfs(r - 1, c);
            dfs(r, c + 1);
            dfs(r, c - 1);
        };
        for (int i = 0; i < m; ++i) {
            dfs(i, 0);
            dfs(i, n - 1);
        }
        for (int j = 0; j < n; ++j) {
            dfs(0, j);
            dfs(m - 1, j);
        }
        int ans = 0;
        for (auto& row : grid) for (int x : row) ans += x;
        return ans;
    }
};

