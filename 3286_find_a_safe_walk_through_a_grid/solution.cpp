// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

#include <array>
#include <queue>
#include <vector>

class Solution {
public:
    bool findSafeWalk(std::vector<std::vector<int>>& grid, int health) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> vis(m, std::vector<int>(n, -1));
        int qh = health - grid[0][0];
        if (qh <= 0) return false;
        std::queue<std::array<int, 3>> q;
        q.push({0, 0, qh});
        vis[0][0] = qh;
        const int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!q.empty()) {
            auto cur = q.front();
            q.pop();
            if (cur[0] == m - 1 && cur[1] == n - 1) return true;
            for (auto& d : dirs) {
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                int nh = cur[2] - grid[nr][nc];
                if (nh <= 0) continue;
                if (nh > vis[nr][nc]) {
                    vis[nr][nc] = nh;
                    q.push({nr, nc, nh});
                }
            }
        }
        return false;
    }
};
