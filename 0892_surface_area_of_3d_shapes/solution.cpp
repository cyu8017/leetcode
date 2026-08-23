// LeetCode 0892 - Surface Area of 3D Shapes
// https://leetcode.com/problems/surface-area-of-3d-shapes/

#include <algorithm>
#include <vector>

class Solution {
public:
    int surfaceArea(std::vector<std::vector<int>>& grid) {
        int n = static_cast<int>(grid.size());
        int area = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j]) {
                    area += grid[i][j] * 4 + 2;
                    if (i) {
                        area -= std::min(grid[i][j], grid[i - 1][j]) * 2;
                    }
                    if (j) {
                        area -= std::min(grid[i][j], grid[i][j - 1]) * 2;
                    }
                }
            }
        }
        return area;
    }
};
