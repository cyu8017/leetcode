// LeetCode 0803 - Bricks Falling When Hit
// https://leetcode.com/problems/bricks-falling-when-hit/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> hitBricks(std::vector<std::vector<int>>& grid,
                               std::vector<std::vector<int>>& hits) {
        int m = static_cast<int>(grid.size());
        int n = static_cast<int>(grid[0].size());
        int roof = m * n;
        std::vector<int> parent(roof + 1), size(roof + 1, 1);
        for (int i = 0; i <= roof; ++i) {
            parent[i] = i;
        }

        auto find = [&](int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };
        auto unite = [&](int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra == rb) {
                return;
            }
            parent[ra] = rb;
            size[rb] += size[ra];
        };
        auto idx = [&](int r, int c) { return r * n + c; };

        std::vector<std::vector<int>> status = grid;
        for (auto& hit : hits) {
            status[hit[0]][hit[1]] = 0;
        }

        const int dr[4] = {-1, 1, 0, 0};
        const int dc[4] = {0, 0, -1, 1};

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (status[r][c] == 0) {
                    continue;
                }
                if (r == 0) {
                    unite(idx(r, c), roof);
                }
                for (int k = 0; k < 4; ++k) {
                    int nr = r + dr[k], nc = c + dc[k];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1) {
                        unite(idx(r, c), idx(nr, nc));
                    }
                }
            }
        }

        std::vector<int> answer(hits.size(), 0);
        for (int i = static_cast<int>(hits.size()) - 1; i >= 0; --i) {
            int r = hits[i][0], c = hits[i][1];
            if (grid[r][c] == 0) {
                continue;
            }
            int prev = size[find(roof)];
            status[r][c] = 1;
            if (r == 0) {
                unite(idx(r, c), roof);
            }
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1) {
                    unite(idx(r, c), idx(nr, nc));
                }
            }
            int curr = size[find(roof)];
            answer[i] = std::max(0, curr - prev - 1);
        }
        return answer;
    }
};
