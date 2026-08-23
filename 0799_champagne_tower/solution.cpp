// LeetCode 0799 - Champagne Tower
// https://leetcode.com/problems/champagne-tower/

#include <algorithm>
#include <vector>

class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        std::vector<double> row{static_cast<double>(poured)};
        for (int r = 0; r < query_row; ++r) {
            std::vector<double> nextRow(r + 2, 0.0);
            for (int i = 0; i < static_cast<int>(row.size()); ++i) {
                double overflow = (row[i] - 1.0) / 2.0;
                if (overflow > 0) {
                    nextRow[i] += overflow;
                    nextRow[i + 1] += overflow;
                }
            }
            row.swap(nextRow);
        }
        return std::min(1.0, row[query_glass]);
    }
};
