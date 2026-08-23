// LeetCode 3111 - Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minRectanglesToCoverPoints(std::vector<std::vector<int>>& points, int w) {
        std::sort(points.begin(), points.end(), [](const auto& a, const auto& b) {
            return a[0] < b[0];
        });
        int ans = 0, x1 = -1;
        for (auto& p : points) {
            if (p[0] > x1) {
                ans++;
                x1 = p[0] + w;
            }
        }
        return ans;
    }
};
