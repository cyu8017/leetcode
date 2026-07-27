// LeetCode 1030 - Matrix Cells in Distance Order
// https://leetcode.com/problems/matrix-cells-in-distance-order/

#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        std::vector<std::vector<int>> cells;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) cells.push_back({r, c});
        }
        std::sort(cells.begin(), cells.end(), [&](const auto& a, const auto& b) {
            return std::abs(a[0] - rCenter) + std::abs(a[1] - cCenter) <
                   std::abs(b[0] - rCenter) + std::abs(b[1] - cCenter);
        });
        return cells;
    }
};

