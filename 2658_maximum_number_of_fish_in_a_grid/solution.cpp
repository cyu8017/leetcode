// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

#include <vector>
#include <functional>
#include <algorithm>

class Solution {
public:
    int findMaxFish(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::function<int(int,int)> dfs = [&](int r, int c) -> int {
            if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) return 0;
            int fish = grid[r][c];
            grid[r][c] = 0;
            return fish + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1);
        };
        int best = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] > 0) best = std::max(best, dfs(i, j));
        return best;
    }
};
