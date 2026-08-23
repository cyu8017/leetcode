// LeetCode 1778 - Shortest Path in a Hidden Grid
// https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

#include <functional>
#include <queue>
#include <set>
#include <utility>
#include <vector>

class Solution {
public:
    int findShortestPath(std::vector<std::vector<int>>& grid) {
        static const int DIRS[4][2] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
        int m = (int)grid.size();
        int n = (int)grid[0].size();
        int r = 0;
        int c = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == -1) {
                    r = i;
                    c = j;
                }
            }
        }

        auto canMove = [&](int d) {
            int nr = r + DIRS[d][0];
            int nc = c + DIRS[d][1];
            return nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != 0;
        };
        auto move = [&](int d) {
            if (canMove(d)) {
                r += DIRS[d][0];
                c += DIRS[d][1];
            }
        };
        auto isTarget = [&]() { return grid[r][c] == 2; };

        std::set<std::pair<int, int>> world;
        world.insert({ 0, 0 });
        bool hasTarget = false;
        std::pair<int, int> target;
        if (isTarget()) {
            return 0;
        }

        std::function<void(int, int)> dfs = [&](int cr, int cc) {
            for (int d = 0; d < 4; d++) {
                if (!canMove(d)) {
                    continue;
                }
                move(d);
                int nr = cr + DIRS[d][0];
                int nc = cc + DIRS[d][1];
                if (!world.count({ nr, nc })) {
                    world.insert({ nr, nc });
                    if (isTarget()) {
                        hasTarget = true;
                        target = { nr, nc };
                    }
                    dfs(nr, nc);
                }
                move(d ^ 1);
            }
        };

        dfs(0, 0);
        if (!hasTarget) {
            return -1;
        }

        std::queue<std::pair<std::pair<int, int>, int>> q;
        q.push({ { 0, 0 }, 0 });
        std::set<std::pair<int, int>> seen;
        seen.insert({ 0, 0 });
        while (!q.empty()) {
            auto [cell, dist] = q.front();
            q.pop();
            if (cell == target) {
                return dist;
            }
            for (auto& dir : DIRS) {
                std::pair<int, int> next = { cell.first + dir[0], cell.second + dir[1] };
                if (world.count(next) && !seen.count(next)) {
                    seen.insert(next);
                    q.push({ next, dist + 1 });
                }
            }
        }
        return -1;
    }
};
