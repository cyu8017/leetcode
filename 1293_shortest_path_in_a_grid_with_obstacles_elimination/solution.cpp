// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
    int shortestPath(std::vector<std::vector<int>>& grid, int k) {
        const int m = static_cast<int>(grid.size());
        const int n = static_cast<int>(grid[0].size());
        if (k >= m + n - 2) {
            return m + n - 2;
        }
        std::queue<std::tuple<int, int, int, int>> q;
        std::unordered_map<long long, int> best;
        auto key = [&](int r, int c) { return static_cast<long long>(r) * n + c; };
        q.push({0, 0, k, 0});
        best[key(0, 0)] = k;
        static const int dr[] = {1, -1, 0, 0};
        static const int dc[] = {0, 0, 1, -1};
        while (!q.empty()) {
            auto [r, c, remaining, distance] = q.front();
            q.pop();
            if (r == m - 1 && c == n - 1) {
                return distance;
            }
            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int nxt = remaining - grid[nr][nc];
                    long long nk = key(nr, nc);
                    if (nxt >= 0 && (!best.count(nk) || nxt > best[nk])) {
                        best[nk] = nxt;
                        q.push({nr, nc, nxt, distance + 1});
                    }
                }
            }
        }
        return -1;
    }
};
