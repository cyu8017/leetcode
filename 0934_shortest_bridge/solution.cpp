// LeetCode 0934 - Shortest Bridge
// https://leetcode.com/problems/shortest-bridge/

#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    int shortestBridge(std::vector<std::vector<int>>& grid) {
        int n = (int)grid.size();
        const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        auto dfs = [&](auto&& self, int r, int c) -> void {
            if (r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1) return;
            grid[r][c] = 2;
            for (auto& d : dirs) self(self, r + d[0], c + d[1]);
        };
        bool found = false;
        for (int i = 0; i < n && !found; i++)
            for (int j = 0; j < n && !found; j++)
                if (grid[i][j] == 1) { dfs(dfs, i, j); found = true; }
        std::queue<std::tuple<int,int,int>> q;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 2) q.emplace(i, j, 0);
        while (!q.empty()) {
            auto [r, c, dist] = q.front();
            q.pop();
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
                if (grid[nr][nc] == 1) return dist;
                if (grid[nr][nc] == 0) {
                    grid[nr][nc] = 2;
                    q.emplace(nr, nc, dist + 1);
                }
            }
        }
        return -1;
    }
};
