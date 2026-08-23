// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    int maximumMinutes(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        const int inf = 1000000000;
        std::vector<std::vector<int>> fire(m, std::vector<int>(n, inf));
        std::queue<std::pair<int, int>> q;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (grid[i][j] == 1) { fire[i][j] = 0; q.push({i, j}); }
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.empty()) {
            auto [r, c] = q.front(); q.pop();
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || fire[nr][nc] != inf) continue;
                fire[nr][nc] = fire[r][c] + 1;
                q.push({nr, nc});
            }
        }
        auto can = [&](int wait) {
            if (wait >= fire[0][0]) return false;
            std::vector<std::vector<char>> vis(m, std::vector<char>(n));
            std::queue<std::tuple<int,int,int>> qq;
            qq.push({0, 0, wait});
            vis[0][0] = 1;
            while (!qq.empty()) {
                auto [r, c, t] = qq.front(); qq.pop();
                for (auto& d : dirs) {
                    int nr = r + d[0], nc = c + d[1], nt = t + 1;
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || vis[nr][nc]) continue;
                    if (nr == m - 1 && nc == n - 1) {
                        if (nt <= fire[nr][nc]) return true;
                        continue;
                    }
                    if (nt >= fire[nr][nc]) continue;
                    vis[nr][nc] = 1;
                    qq.push({nr, nc, nt});
                }
            }
            return false;
        };
        int lo = 0, hi = m * n + 10, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (can(mid)) { ans = mid; lo = mid + 1; }
            else hi = mid - 1;
        }
        if (ans >= m * n) return inf;
        return ans;
    }
};
