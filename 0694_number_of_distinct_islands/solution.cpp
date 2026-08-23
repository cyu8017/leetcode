// LeetCode 0694 - Number of Distinct Islands
// https://leetcode.com/problems/number-of-distinct-islands/

#include <set>
#include <utility>
#include <vector>

class Solution {
    void dfs(std::vector<std::vector<int>>& grid, int r, int c, int br, int bc,
             std::vector<std::pair<int, int>>& path) {
        if (r < 0 || r >= static_cast<int>(grid.size()) || c < 0 ||
            c >= static_cast<int>(grid[0].size()) || grid[r][c] == 0) {
            return;
        }
        grid[r][c] = 0;
        path.emplace_back(r - br, c - bc);
        dfs(grid, r + 1, c, br, bc, path);
        dfs(grid, r - 1, c, br, bc, path);
        dfs(grid, r, c + 1, br, bc, path);
        dfs(grid, r, c - 1, br, bc, path);
    }

public:
    int numDistinctIslands(std::vector<std::vector<int>>& grid) {
        if (grid.empty()) {
            return 0;
        }
        std::set<std::vector<std::pair<int, int>>> shapes;
        for (int i = 0; i < static_cast<int>(grid.size()); ++i) {
            for (int j = 0; j < static_cast<int>(grid[0].size()); ++j) {
                if (grid[i][j] == 1) {
                    std::vector<std::pair<int, int>> path;
                    dfs(grid, i, j, i, j, path);
                    shapes.insert(path);
                }
            }
        }
        return static_cast<int>(shapes.size());
    }
};
