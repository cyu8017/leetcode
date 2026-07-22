// LeetCode 1610 - Maximum Number of Visible Points
// https://leetcode.com/problems/maximum-number-of-visible-points/

#include <algorithm>
#include <cmath>
#include <vector>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

class Solution {
public:
    int visiblePoints(std::vector<std::vector<int>>& points, int angle, std::vector<int>& location) {
        int same = 0;
        std::vector<double> a;
        for (const auto& p : points) {
            const int dx = p[0] - location[0];
            const int dy = p[1] - location[1];
            if (dx == 0 && dy == 0) {
                ++same;
            } else {
                a.push_back(std::atan2(dy, dx));
            }
        }
        std::sort(a.begin(), a.end());
        const int n = static_cast<int>(a.size());
        std::vector<double> ext = a;
        for (double x : a) {
            ext.push_back(x + 2 * M_PI);
        }
        const double width = angle * M_PI / 180.0 + 1e-12;
        int left = 0, best = 0;
        for (int right = 0; right < static_cast<int>(ext.size()); ++right) {
            while (ext[right] - ext[left] > width) {
                ++left;
            }
            best = std::max(best, std::min(n, right - left + 1));
        }
        return best + same;
    }
};
