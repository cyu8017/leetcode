// LeetCode 0463 - Island Perimeter
// https://leetcode.com/problems/island-perimeter/

#include <vector>

class Solution {
public:
    int islandPerimeter(std::vector<std::vector<int>>& grid) {
        int rows = static_cast<int>(grid.size());
        int cols = static_cast<int>(grid[0].size());
        int perimeter = 0;
        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                if (grid[row][col] == 0) {
                    continue;
                }
                perimeter += 4;
                if (row > 0 && grid[row - 1][col]) {
                    perimeter -= 2;
                }
                if (col > 0 && grid[row][col - 1]) {
                    perimeter -= 2;
                }
            }
        }
        return perimeter;
    }
};
