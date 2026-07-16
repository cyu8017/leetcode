// LeetCode 0469 - Convex Polygon
// https://leetcode.com/problems/convex-polygon/

#include <vector>

class Solution {
public:
    bool isConvex(std::vector<std::vector<int>>& points) {
        int direction = 0;
        int count = static_cast<int>(points.size());
        for (int index = 0; index < count; ++index) {
            int x1 = points[(index + 1) % count][0] - points[index][0];
            int y1 = points[(index + 1) % count][1] - points[index][1];
            int x2 = points[(index + 2) % count][0] - points[(index + 1) % count][0];
            int y2 = points[(index + 2) % count][1] - points[(index + 1) % count][1];
            long long cross = static_cast<long long>(x1) * y2 - static_cast<long long>(y1) * x2;
            if (cross == 0) {
                continue;
            }
            int current = cross > 0 ? 1 : -1;
            if (direction == 0) {
                direction = current;
            } else if (direction != current) {
                return false;
            }
        }
        return true;
    }
};
