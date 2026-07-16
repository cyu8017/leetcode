// LeetCode 0296 - Best Meeting Point
// https://leetcode.com/problems/best-meeting-point/

#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    int minTotalDistance(std::vector<std::vector<int>>& grid) {
        std::vector<int> rows;
        std::vector<int> cols;

        for (int rowIndex = 0; rowIndex < static_cast<int>(grid.size()); rowIndex++) {
            for (int colIndex = 0; colIndex < static_cast<int>(grid[rowIndex].size()); colIndex++) {
                if (grid[rowIndex][colIndex] == 1) {
                    rows.push_back(rowIndex);
                    cols.push_back(colIndex);
                }
            }
        }

        std::sort(cols.begin(), cols.end());
        int rowMedian = rows[rows.size() / 2];
        int colMedian = cols[cols.size() / 2];

        int total = 0;
        for (int row : rows) {
            total += std::abs(row - rowMedian);
        }
        for (int col : cols) {
            total += std::abs(col - colMedian);
        }
        return total;
    }
};
