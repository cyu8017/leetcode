// LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

#include <queue>
#include <vector>

class Solution {
public:
    int minimumTime(std::vector<std::vector<int>>& grid) {
        if (grid[0][1] > 1 && grid[1][0] > 1) return -1;
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> dist(m, std::vector<int>(n, 1 << 30));
        using Item = std::tuple<int, int, int>;
        std::priority_queue<Item, std::vector<Item>, std::greater<Item>> h;
        h.push({0, 0, 0});
        dist[0][0] = 0;
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!h.empty()) {
            auto [t, r, c] = h.top();
            h.pop();
            if (r == m - 1 && c == n - 1) return t;
            if (t > dist[r][c]) continue;
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int nt = t + 1;
                if (nt < grid[nr][nc]) {
                    int wait = grid[nr][nc] - nt;
                    if (wait % 2 == 1) wait++;
                    nt += wait;
                }
                if (nt < dist[nr][nc]) {
                    dist[nr][nc] = nt;
                    h.push({nt, nr, nc});
                }
            }
        }
        return -1;
    }
};
