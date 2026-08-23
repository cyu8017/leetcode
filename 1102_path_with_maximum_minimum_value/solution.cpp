// LeetCode 1102 - Path With Maximum Minimum Value
// https://leetcode.com/problems/path-with-maximum-minimum-value/

#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int maximumMinimumPath(std::vector<std::vector<int>>& grid) {
        const int m = static_cast<int>(grid.size());
        const int n = static_cast<int>(grid[0].size());
        using Node = std::pair<int, std::pair<int, int>>;
        std::priority_queue<Node> heap;
        heap.push({grid[0][0], {0, 0}});
        std::vector<std::vector<char>> seen(m, std::vector<char>(n, 0));
        seen[0][0] = 1;
        static const int dr[4] = {1, -1, 0, 0};
        static const int dc[4] = {0, 0, 1, -1};
        while (!heap.empty()) {
            auto [val, pos] = heap.top();
            heap.pop();
            int r = pos.first;
            int c = pos.second;
            if (r == m - 1 && c == n - 1) {
                return val;
            }
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen[nr][nc]) {
                    seen[nr][nc] = 1;
                    heap.push({std::min(val, grid[nr][nc]), {nr, nc}});
                }
            }
        }
        return grid[0][0];
    }
};
