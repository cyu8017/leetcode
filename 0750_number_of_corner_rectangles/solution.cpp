// LeetCode 0750 - Number Of Corner Rectangles
// https://leetcode.com/problems/number-of-corner-rectangles/

#include <vector>

class Solution {
public:
    int countCornerRectangles(std::vector<std::vector<int>>& grid) {
        int m = static_cast<int>(grid.size());
        int n = static_cast<int>(grid[0].size());
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = i + 1; j < m; ++j) {
                int count = 0;
                for (int c = 0; c < n; ++c) {
                    if (grid[i][c] && grid[j][c]) {
                        ++count;
                    }
                }
                ans += count * (count - 1) / 2;
            }
        }
        return ans;
    }
};
