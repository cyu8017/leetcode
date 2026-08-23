// LeetCode 0356 - Line Reflection
// https://leetcode.com/problems/line-reflection/

#include <algorithm>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution {
public:
    bool isReflected(std::vector<std::vector<int>>& points) {
        std::unordered_set<std::string> pointSet;
        int minX = points[0][0];
        int maxX = points[0][0];

        for (const auto& point : points) {
            minX = std::min(minX, point[0]);
            maxX = std::max(maxX, point[0]);
            pointSet.insert(std::to_string(point[0]) + "," + std::to_string(point[1]));
        }

        int target = minX + maxX;
        for (const auto& point : points) {
            std::string mirror = std::to_string(target - point[0]) + "," + std::to_string(point[1]);
            if (pointSet.find(mirror) == pointSet.end()) {
                return false;
            }
        }

        return true;
    }
};
