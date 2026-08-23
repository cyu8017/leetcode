// LeetCode 0675 - Cut Off Trees for Golf Event
// https://leetcode.com/problems/cut-off-trees-for-golf-event/

#include <algorithm>
#include <queue>
#include <tuple>
#include <utility>
#include <vector>

class Solution {
    int bfs(const std::vector<std::vector<int>>& forest, int sr, int sc, int tr, int tc) {
        if (sr == tr && sc == tc) {
            return 0;
        }
        const int m = static_cast<int>(forest.size());
        const int n = static_cast<int>(forest[0].size());
        std::vector<std::vector<bool>> seen(m, std::vector<bool>(n, false));
        std::queue<std::tuple<int, int, int>> queue;
        queue.emplace(sr, sc, 0);
        seen[sr][sc] = true;
        static const int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!queue.empty()) {
            auto [r, c, dist] = queue.front();
            queue.pop();
            for (const auto& dir : dirs) {
                const int nr = r + dir[0];
                const int nc = c + dir[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || seen[nr][nc] ||
                    forest[nr][nc] == 0) {
                    continue;
                }
                if (nr == tr && nc == tc) {
                    return dist + 1;
                }
                seen[nr][nc] = true;
                queue.emplace(nr, nc, dist + 1);
            }
        }
        return -1;
    }

public:
    int cutOffTree(std::vector<std::vector<int>>& forest) {
        std::vector<std::tuple<int, int, int>> trees;
        for (int i = 0; i < static_cast<int>(forest.size()); ++i) {
            for (int j = 0; j < static_cast<int>(forest[0].size()); ++j) {
                if (forest[i][j] > 1) {
                    trees.emplace_back(forest[i][j], i, j);
                }
            }
        }
        std::sort(trees.begin(), trees.end());
        int sr = 0;
        int sc = 0;
        int steps = 0;
        for (const auto& [_, tr, tc] : trees) {
            const int dist = bfs(forest, sr, sc, tr, tc);
            if (dist < 0) {
                return -1;
            }
            steps += dist;
            sr = tr;
            sc = tc;
        }
        return steps;
    }
};
