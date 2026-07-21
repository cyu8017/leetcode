// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxBuilding(int n, const std::vector<std::vector<int>>& restrictions) {
        std::vector<std::vector<int>> points = {{1, 0}};
        points.insert(points.end(), restrictions.begin(), restrictions.end());
        std::sort(points.begin(), points.end());
        if (points.back()[0] != n) {
            points.push_back({n, n - 1});
        }

        for (size_t i = 1; i < points.size(); ++i) {
            int prevId = points[i - 1][0];
            int prevHeight = points[i - 1][1];
            int currId = points[i][0];
            points[i][1] = std::min(points[i][1], prevHeight + currId - prevId);
        }
        for (int i = static_cast<int>(points.size()) - 2; i >= 0; --i) {
            int nextId = points[i + 1][0];
            int nextHeight = points[i + 1][1];
            int currId = points[i][0];
            points[i][1] = std::min(points[i][1], nextHeight + nextId - currId);
        }

        int best = 0;
        for (const auto& point : points) {
            best = std::max(best, point[1]);
        }
        for (size_t i = 0; i + 1 < points.size(); ++i) {
            int id1 = points[i][0];
            int h1 = points[i][1];
            int id2 = points[i + 1][0];
            int h2 = points[i + 1][1];
            best = std::max(best, (h1 + h2 + id2 - id1) / 2);
        }
        return best;
    }
};
