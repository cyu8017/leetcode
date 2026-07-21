// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

#include <limits>
#include <functional>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    // Test harness passes the revealed grid plus start/target coordinates.
    int findShortestPath(std::vector<std::vector<int>>& grid, int r1, int c1, int r2, int c2) {
        if (r1 == r2 && c1 == c2) {
            return 0;
        }
        const int m = static_cast<int>(grid.size());
        const int n = static_cast<int>(grid[0].size());
        static const int DIRS[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        std::vector<std::vector<int>> dist(m, std::vector<int>(n, std::numeric_limits<int>::max()));
        using Node = std::pair<int, std::pair<int, int>>;
        std::priority_queue<Node, std::vector<Node>, std::greater<>> heap;
        dist[r1][c1] = 0;
        heap.push({0, {r1, c1}});

        while (!heap.empty()) {
            auto [d, pos] = heap.top();
            heap.pop();
            auto [r, c] = pos;
            if (r == r2 && c == c2) {
                return d;
            }
            if (d > dist[r][c]) {
                continue;
            }
            for (const auto& dir : DIRS) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 0) {
                    continue;
                }
                int nd = d + grid[nr][nc];
                if (nd < dist[nr][nc]) {
                    dist[nr][nc] = nd;
                    heap.push({nd, {nr, nc}});
                }
            }
        }
        return -1;
    }
};
