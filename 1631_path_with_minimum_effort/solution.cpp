// LeetCode 1631 - Path With Minimum Effort
// https://leetcode.com/problems/path-with-minimum-effort/

#include <cmath>
#include <climits>
#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    int minimumEffortPath(std::vector<std::vector<int>>& heights) {
        const int m = static_cast<int>(heights.size());
        const int n = static_cast<int>(heights[0].size());
        std::vector<std::vector<int>> dist(m, std::vector<int>(n, INT_MAX));
        dist[0][0] = 0;
        using State = std::tuple<int, int, int>;
        std::priority_queue<State, std::vector<State>, std::greater<>> heap;
        heap.push({0, 0, 0});
        const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!heap.empty()) {
            auto [effort, i, j] = heap.top();
            heap.pop();
            if (i == m - 1 && j == n - 1) {
                return effort;
            }
            if (effort != dist[i][j]) {
                continue;
            }
            for (auto& d : dirs) {
                const int x = i + d[0], y = j + d[1];
                if (x >= 0 && x < m && y >= 0 && y < n) {
                    const int nd = std::max(effort, std::abs(heights[i][j] - heights[x][y]));
                    if (nd < dist[x][y]) {
                        dist[x][y] = nd;
                        heap.push({nd, x, y});
                    }
                }
            }
        }
        return 0;
    }
};
