// LeetCode 0864 - Shortest Path to Get All Keys
// https://leetcode.com/problems/shortest-path-to-get-all-keys/

#include <queue>
#include <string>
#include <tuple>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int shortestPathAllKeys(std::vector<std::string>& grid) {
        int m = static_cast<int>(grid.size());
        int n = static_cast<int>(grid[0].size());
        int allKeys = 0;
        int sr = 0, sc = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '@') {
                    sr = i;
                    sc = j;
                } else if (grid[i][j] >= 'a' && grid[i][j] <= 'f') {
                    allKeys |= 1 << (grid[i][j] - 'a');
                }
            }
        }
        std::queue<std::tuple<int, int, int, int>> queue;
        queue.push({sr, sc, 0, 0});
        auto encode = [](int r, int c, int mask) {
            return (static_cast<long long>(r) << 20) | (static_cast<long long>(c) << 10) |
                   mask;
        };
        std::unordered_set<long long> seen{encode(sr, sc, 0)};
        const int dr[4] = {1, -1, 0, 0};
        const int dc[4] = {0, 0, 1, -1};
        while (!queue.empty()) {
            auto [r, c, mask, dist] = queue.front();
            queue.pop();
            if (mask == allKeys) {
                return dist;
            }
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == '#') {
                    continue;
                }
                char cell = grid[nr][nc];
                int nmask = mask;
                if (cell >= 'a' && cell <= 'f') {
                    nmask |= 1 << (cell - 'a');
                }
                if (cell >= 'A' && cell <= 'F' && !(mask & (1 << (cell - 'A')))) {
                    continue;
                }
                long long state = encode(nr, nc, nmask);
                if (!seen.count(state)) {
                    seen.insert(state);
                    queue.push({nr, nc, nmask, dist + 1});
                }
            }
        }
        return -1;
    }
};
