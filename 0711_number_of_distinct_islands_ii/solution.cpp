// LeetCode 0711 - Number of Distinct Islands II
// https://leetcode.com/problems/number-of-distinct-islands-ii/

#include <algorithm>
#include <set>
#include <vector>

class Solution {
public:
    int numDistinctIslands2(std::vector<std::vector<int>>& grid) {
        if (grid.empty()) {
            return 0;
        }
        int m = static_cast<int>(grid.size());
        int n = static_cast<int>(grid[0].size());
        std::set<std::vector<std::pair<int, int>>> shapes;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    std::vector<std::pair<int, int>> cells;
                    dfs(grid, i, j, m, n, cells);
                    shapes.insert(canonical(cells));
                }
            }
        }
        return static_cast<int>(shapes.size());
    }

private:
    void dfs(std::vector<std::vector<int>>& grid, int r, int c, int m, int n,
             std::vector<std::pair<int, int>>& cells) {
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) {
            return;
        }
        grid[r][c] = 0;
        cells.push_back({r, c});
        static const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (auto& d : dirs) {
            dfs(grid, r + d[0], c + d[1], m, n, cells);
        }
    }

    std::vector<std::pair<int, int>> canonical(const std::vector<std::pair<int, int>>& cells) {
        using Transform = std::pair<int, int> (*)(int, int);
        Transform transforms[8] = {
            [](int x, int y) { return std::pair<int, int>{x, y}; },
            [](int x, int y) { return std::pair<int, int>{x, -y}; },
            [](int x, int y) { return std::pair<int, int>{-x, y}; },
            [](int x, int y) { return std::pair<int, int>{-x, -y}; },
            [](int x, int y) { return std::pair<int, int>{y, x}; },
            [](int x, int y) { return std::pair<int, int>{y, -x}; },
            [](int x, int y) { return std::pair<int, int>{-y, x}; },
            [](int x, int y) { return std::pair<int, int>{-y, -x}; },
        };
        std::vector<std::vector<std::pair<int, int>>> norms;
        for (auto transform : transforms) {
            std::vector<std::pair<int, int>> pts;
            pts.reserve(cells.size());
            for (auto [x, y] : cells) {
                pts.push_back(transform(x, y));
            }
            int minX = pts[0].first, minY = pts[0].second;
            for (auto [x, y] : pts) {
                minX = std::min(minX, x);
                minY = std::min(minY, y);
            }
            for (auto& p : pts) {
                p.first -= minX;
                p.second -= minY;
            }
            std::sort(pts.begin(), pts.end());
            norms.push_back(std::move(pts));
        }
        return *std::min_element(norms.begin(), norms.end());
    }
};
