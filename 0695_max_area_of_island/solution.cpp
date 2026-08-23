// LeetCode 0695 - Max Area of Island
// https://leetcode.com/problems/max-area-of-island/

#include <algorithm>
#include <vector>

class Solution {
    int dfs(std::vector<std::vector<int>>& grid, int r, int c) {
        if (r < 0 || r >= static_cast<int>(grid.size()) || c < 0 ||
            c >= static_cast<int>(grid[0].size()) || grid[r][c] == 0) {
            return 0;
        }
        grid[r][c] = 0;
        return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) +
               dfs(grid, r, c - 1);
    }

public:
    int maxAreaOfIsland(std::vector<std::vector<int>>& grid) {
        int best = 0;
        for (int i = 0; i < static_cast<int>(grid.size()); ++i) {
            for (int j = 0; j < static_cast<int>(grid[0].size()); ++j) {
                best = std::max(best, dfs(grid, i, j));
            }
        }
        return best;
    }
};
