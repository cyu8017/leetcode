// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maxIncreasingCells(std::vector<std::vector<int>>& mat) {
        int m = (int)mat.size(), n = (int)mat[0].size();
        struct Cell { int v, r, c; };
        std::vector<Cell> cells;
        cells.reserve(m * n);
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                cells.push_back({mat[i][j], i, j});
        std::sort(cells.begin(), cells.end(), [](auto& a, auto& b) { return a.v < b.v; });
        std::vector<int> rowMax(m), colMax(n);
        std::vector<std::vector<int>> dp(m, std::vector<int>(n));
        int ans = 0;
        for (int i = 0; i < (int)cells.size(); ) {
            int j = i;
            while (j < (int)cells.size() && cells[j].v == cells[i].v) j++;
            std::vector<std::tuple<int,int,int>> buf;
            for (int k = i; k < j; k++) {
                int r = cells[k].r, c = cells[k].c;
                int best = std::max(rowMax[r], colMax[c]);
                dp[r][c] = best + 1;
                ans = std::max(ans, dp[r][c]);
                buf.push_back({r, c, dp[r][c]});
            }
            for (auto [r, c, val] : buf) {
                rowMax[r] = std::max(rowMax[r], val);
                colMax[c] = std::max(colMax[c], val);
            }
            i = j;
        }
        return ans;
    }
};
