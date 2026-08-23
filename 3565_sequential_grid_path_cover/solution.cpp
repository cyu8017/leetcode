// LeetCode 3565 - Sequential Grid Path Cover
// https://leetcode.com/problems/sequential-grid-path-cover/

#include <cstdint>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> findPath(std::vector<std::vector<int>>& grid, int k) {
        (void)k;
        int m = (int)grid.size(), n = (int)grid[0].size();
        uint64_t st = 0;
        std::vector<std::vector<int>> path;
        int dirs[5] = {-1, 0, 1, 0, -1};
        auto f = [&](int i, int j) { return i * n + j; };

        auto dfs = [&](auto&& self, int i, int j, int v) -> bool {
            path.push_back({i, j});
            if ((int)path.size() == m * n) return true;
            int idx = f(i, j);
            st |= 1ULL << idx;
            if (grid[i][j] == v) v++;
            for (int t = 0; t < 4; t++) {
                int x = i + dirs[t], y = j + dirs[t + 1];
                if (0 <= x && x < m && 0 <= y && y < n) {
                    int idx2 = f(x, y);
                    if (((st >> idx2) & 1ULL) == 0 && (grid[x][y] == 0 || grid[x][y] == v)) {
                        if (self(self, x, y, v)) return true;
                    }
                }
            }
            path.pop_back();
            st ^= 1ULL << idx;
            return false;
        };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 || grid[i][j] == 1) {
                    if (dfs(dfs, i, j, 1)) return path;
                    path.clear();
                    st = 0;
                }
            }
        }
        return {};
    }
};
