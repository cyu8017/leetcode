// LeetCode 3195 - Find the Minimum Area to Cover All Ones I
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

#include <vector>
#include <algorithm>

class Solution {
public:
    int minimumArea(std::vector<std::vector<int>>& grid) {
        int x1 = (int)grid.size(), y1 = (int)grid[0].size(), x2 = 0, y2 = 0;
        for (int i = 0; i < (int)grid.size(); i++) {
            for (int j = 0; j < (int)grid[0].size(); j++) {
                if (grid[i][j] == 1) {
                    x1 = std::min(x1, i); y1 = std::min(y1, j);
                    x2 = std::max(x2, i); y2 = std::max(y2, j);
                }
            }
        }
        return (x2 - x1 + 1) * (y2 - y1 + 1);
    }
};
