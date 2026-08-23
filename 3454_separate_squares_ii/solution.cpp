// LeetCode 3454 - Separate Squares II
// https://leetcode.com/problems/separate-squares-ii/

#include <vector>

class Solution {
public:
    double separateSquares(std::vector<std::vector<int>>& squares) {
        double total = 0;
        for (auto& sq : squares) {
            double l = sq[2];
            total += l * l;
        }
        auto areaBelow = [&](double y) {
            double below = 0;
            for (auto& sq : squares) {
                double yi = sq[1], l = sq[2];
                double top = yi + l;
                if (y <= yi) continue;
                else if (y >= top) below += l * l;
                else below += l * (y - yi);
            }
            return below;
        };
        double lo = 0.0, hi = 2e9;
        for (int it = 0; it < 60; it++) {
            double mid = (lo + hi) / 2;
            if (areaBelow(mid) * 2 < total) lo = mid;
            else hi = mid;
        }
        return hi;
    }
};
