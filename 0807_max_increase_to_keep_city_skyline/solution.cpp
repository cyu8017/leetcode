// LeetCode 0807 - Max Increase to Keep City Skyline
// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxIncreaseKeepingSkyline(std::vector<std::vector<int>>& grid) {
        int m = static_cast<int>(grid.size());
        int n = static_cast<int>(grid[0].size());
        std::vector<int> rowMax(m, 0), colMax(n, 0);
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                rowMax[r] = std::max(rowMax[r], grid[r][c]);
                colMax[c] = std::max(colMax[c], grid[r][c]);
            }
        }
        int ans = 0;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                ans += std::min(rowMax[r], colMax[c]) - grid[r][c];
            }
        }
        return ans;
    }
};
