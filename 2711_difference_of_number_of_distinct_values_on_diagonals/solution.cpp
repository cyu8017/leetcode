// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

#include <vector>
#include <unordered_set>
#include <cstdlib>

class Solution {
public:
    std::vector<std::vector<int>> differenceOfDistinctValues(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> ans(m, std::vector<int>(n));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                std::unordered_set<int> top, bot;
                for (int r = i - 1, c = j - 1; r >= 0 && c >= 0; r--, c--) top.insert(grid[r][c]);
                for (int r = i + 1, c = j + 1; r < m && c < n; r++, c++) bot.insert(grid[r][c]);
                ans[i][j] = std::abs((int)top.size() - (int)bot.size());
            }
        }
        return ans;
    }
};
