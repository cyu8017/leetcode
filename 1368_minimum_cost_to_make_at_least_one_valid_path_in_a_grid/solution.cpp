#include <deque>
#include <vector>

class Solution {
public:
    int minCost(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        const int INF = 1e9;
        std::vector<std::vector<int>> dist(m, std::vector<int>(n, INF));
        dist[0][0] = 0;
        std::deque<std::pair<int, int>> q;
        q.push_back({0, 0});
        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!q.empty()) {
            auto [r, c] = q.front(); q.pop_front();
            for (int k = 0; k < 4; ++k) {
                int x = r + dirs[k][0], y = c + dirs[k][1];
                if (x >= 0 && x < m && y >= 0 && y < n) {
                    int w = (k + 1) != grid[r][c];
                    int nd = dist[r][c] + w;
                    if (nd < dist[x][y]) {
                        dist[x][y] = nd;
                        if (w) q.push_back({x, y});
                        else q.push_front({x, y});
                    }
                }
            }
        }
        return dist[m - 1][n - 1];
    }
};
