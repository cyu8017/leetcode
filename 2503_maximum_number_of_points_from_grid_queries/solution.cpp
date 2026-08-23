// LeetCode 2503 - Maximum Number of Points From Grid Queries
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

#include <algorithm>
#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    std::vector<int> maxPoints(std::vector<std::vector<int>>& grid, std::vector<int>& queries) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<int> order(queries.size());
        for (int i = 0; i < (int)order.size(); i++) order[i] = i;
        std::sort(order.begin(), order.end(), [&](int a, int b) { return queries[a] < queries[b]; });
        std::vector<int> ans(queries.size());
        std::vector<std::vector<char>> visited(m, std::vector<char>(n, 0));
        using Cell = std::tuple<int, int, int>;
        std::priority_queue<Cell, std::vector<Cell>, std::greater<Cell>> pq;
        pq.push({grid[0][0], 0, 0});
        visited[0][0] = 1;
        int points = 0;
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int qi : order) {
            int q = queries[qi];
            while (!pq.empty() && std::get<0>(pq.top()) < q) {
                auto [v, r, c] = pq.top();
                (void)v;
                pq.pop();
                points++;
                for (auto& d : dirs) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {
                        visited[nr][nc] = 1;
                        pq.push({grid[nr][nc], nr, nc});
                    }
                }
            }
            ans[qi] = points;
        }
        return ans;
    }
};
