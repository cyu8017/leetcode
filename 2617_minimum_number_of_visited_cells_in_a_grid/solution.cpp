// LeetCode 2617 - Minimum Number of Visited Cells in a Grid
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

#include <queue>
#include <vector>

class Solution {
public:
    int minimumVisitedCells(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> dist(m, std::vector<int>(n, -1));
        std::queue<std::pair<int, int>> q;
        q.push({0, 0});
        dist[0][0] = 1;
        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();
            if (r == m - 1 && c == n - 1) return dist[r][c];
            for (int nc = c + 1; nc <= c + grid[r][c] && nc < n; ++nc) {
                if (dist[r][nc] == -1) {
                    dist[r][nc] = dist[r][c] + 1;
                    q.push({r, nc});
                }
            }
            for (int nr = r + 1; nr <= r + grid[r][c] && nr < m; ++nr) {
                if (dist[nr][c] == -1) {
                    dist[nr][c] = dist[r][c] + 1;
                    q.push({nr, c});
                }
            }
        }
        return -1;
    }
};
