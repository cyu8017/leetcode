// LeetCode 1779 - Find Nearest Point That Has the Same X or Y Coordinate
// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

#include <climits>
#include <cstdlib>
#include <vector>

class Solution {
public:
    int nearestValidPoint(int x, int y, std::vector<std::vector<int>>& points) {
        int best = INT_MAX;
        int ans = -1;
        for (int i = 0; i < (int)points.size(); i++) {
            int px = points[i][0];
            int py = points[i][1];
            if (px != x && py != y) {
                continue;
            }
            int dist = std::abs(px - x) + std::abs(py - y);
            if (dist < best) {
                best = dist;
                ans = i;
            }
        }
        return ans;
    }
};
