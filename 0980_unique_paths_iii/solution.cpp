// LeetCode 0980 - Unique Paths III
// https://leetcode.com/problems/unique-paths-iii/

#include <vector>

class Solution {
public:
    int uniquePathsIII(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        int empty = 0, sr = 0, sc = 0, ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != -1) empty++;
                if (grid[i][j] == 1) { sr = i; sc = j; }
            }
        }
        auto dfs = [&](auto&& self, int r, int c, int remain) -> void {
            if (grid[r][c] == 2) {
                if (remain == 1) ans++;
                return;
            }
            int temp = grid[r][c];
            grid[r][c] = -1;
            const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != -1)
                    self(self, nr, nc, remain - 1);
            }
            grid[r][c] = temp;
        };
        dfs(dfs, sr, sc, empty);
        return ans;
    }
};
