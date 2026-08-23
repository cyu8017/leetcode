// LeetCode 2371 - Minimize Maximum Value in a Grid
// https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> minScore(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        struct Cell { int v, r, c; };
        std::vector<Cell> arr;
        arr.reserve(m * n);
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                arr.push_back({grid[i][j], i, j});
        std::sort(arr.begin(), arr.end(), [](const Cell& a, const Cell& b) { return a.v < b.v; });
        std::vector<int> rowMax(m), colMax(n);
        std::vector<std::vector<int>> ans(m, std::vector<int>(n));
        for (auto& cel : arr) {
            int val = std::max(rowMax[cel.r], colMax[cel.c]) + 1;
            ans[cel.r][cel.c] = val;
            rowMax[cel.r] = val;
            colMax[cel.c] = val;
        }
        return ans;
    }
};
