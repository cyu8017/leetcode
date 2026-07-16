// LeetCode 0391 - Perfect Rectangle
// https://leetcode.com/problems/perfect-rectangle/

#include <algorithm>
#include <climits>
#include <map>
#include <utility>
#include <vector>

class Solution {
public:
    bool isRectangleCover(std::vector<std::vector<int>>& rectangles) {
        std::map<std::pair<int, int>, int> points;
        long long area = 0;
        int minX = INT_MAX;
        int minY = INT_MAX;
        int maxX = INT_MIN;
        int maxY = INT_MIN;

        for (const auto& rect : rectangles) {
            int x1 = rect[0];
            int y1 = rect[1];
            int x2 = rect[2];
            int y2 = rect[3];
            area += static_cast<long long>(x2 - x1) * (y2 - y1);
            minX = std::min(minX, x1);
            minY = std::min(minY, y1);
            maxX = std::max(maxX, x2);
            maxY = std::max(maxY, y2);

            for (auto point :
                 {std::make_pair(x1, y1), std::make_pair(x1, y2), std::make_pair(x2, y1),
                  std::make_pair(x2, y2)}) {
                points[point] ^= 1;
            }
        }

        if (points.size() != 4) {
            return false;
        }
        if (!points[{minX, minY}] || !points[{minX, maxY}] || !points[{maxX, minY}] ||
            !points[{maxX, maxY}]) {
            return false;
        }
        for (const auto& entry : points) {
            if (entry.second != 1) {
                return false;
            }
        }

        return area == static_cast<long long>(maxX - minX) * (maxY - minY);
    }
};
