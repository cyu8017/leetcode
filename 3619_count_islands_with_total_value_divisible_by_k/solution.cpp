// LeetCode 3619 - Count Islands With Total Value Divisible by K
// https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

#include <vector>

class Solution {
public:
    int countIslands(std::vector<std::vector<int>>& grid, int k) {
        int m = (int)grid.size(), n = (int)grid[0].size(), ans = 0;
        int dirs[5] = {-1, 0, 1, 0, -1};
        auto dfs = [&](auto&& self, int i, int j) -> long long {
            long long s = grid[i][j];
            grid[i][j] = 0;
            for (int d = 0; d < 4; d++) {
                int x = i + dirs[d], y = j + dirs[d + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] > 0) s += self(self, x, y);
            }
            return s;
        };
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] > 0 && dfs(dfs, i, j) % k == 0) ans++;
        return ans;
    }
};
