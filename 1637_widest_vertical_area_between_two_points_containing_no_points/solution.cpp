// LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points
// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxWidthOfVerticalArea(std::vector<std::vector<int>>& points) {
        std::vector<int> xs;
        xs.reserve(points.size());
        for (const auto& p : points) {
            xs.push_back(p[0]);
        }
        std::sort(xs.begin(), xs.end());
        int ans = 0;
        for (size_t i = 1; i < xs.size(); ++i) {
            ans = std::max(ans, xs[i] - xs[i - 1]);
        }
        return ans;
    }
};
