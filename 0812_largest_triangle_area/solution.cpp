// LeetCode 0812 - Largest Triangle Area
// https://leetcode.com/problems/largest-triangle-area/

#include <cmath>
#include <vector>

class Solution {
public:
    double largestTriangleArea(std::vector<std::vector<int>>& points) {
        double best = 0.0;
        int n = static_cast<int>(points.size());
        for (int i = 0; i < n; ++i) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                int x2 = points[j][0], y2 = points[j][1];
                for (int k = j + 1; k < n; ++k) {
                    int x3 = points[k][0], y3 = points[k][1];
                    double area =
                        std::abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) /
                        2.0;
                    best = std::max(best, area);
                }
            }
        }
        return best;
    }
};
