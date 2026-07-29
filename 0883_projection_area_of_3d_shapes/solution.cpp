// LeetCode 0883 - Projection Area of 3D Shapes
// https://leetcode.com/problems/projection-area-of-3d-shapes/

#include <algorithm>
#include <vector>

class Solution {
public:
    int projectionArea(std::vector<std::vector<int>>& grid) {
        int n = static_cast<int>(grid.size());
        int top = 0, front = 0, side = 0;
        for (int i = 0; i < n; ++i) {
            int rowMax = 0, colMax = 0;
            for (int j = 0; j < n; ++j) {
                if (grid[i][j]) {
                    ++top;
                }
                rowMax = std::max(rowMax, grid[i][j]);
                colMax = std::max(colMax, grid[j][i]);
            }
            front += rowMax;
            side += colMax;
        }
        return top + front + side;
    }
};
