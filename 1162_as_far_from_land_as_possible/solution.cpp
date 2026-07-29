// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int maxDistance(std::vector<std::vector<int>>& grid) {
        int n = static_cast<int>(grid.size());
        std::queue<std::pair<int, int>> q;
        for (int r = 0; r < n; ++r)
            for (int c = 0; c < n; ++c)
                if (grid[r][c] == 1) q.emplace(r, c);
        if (q.empty() || static_cast<int>(q.size()) == n * n) return -1;
        int dist = -1;
        const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.empty()) {
            ++dist;
            int sz = static_cast<int>(q.size());
            for (int i = 0; i < sz; ++i) {
                auto [r, c] = q.front(); q.pop();
                for (auto& d : dirs) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                        grid[nr][nc] = 1;
                        q.emplace(nr, nc);
                    }
                }
            }
        }
        return dist;
    }
};
