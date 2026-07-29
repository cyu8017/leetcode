#include <algorithm>

class Solution {
public:
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int x = std::min(std::max(xCenter, x1), x2);
        int y = std::min(std::max(yCenter, y1), y2);
        long long dx = x - xCenter, dy = y - yCenter;
        return dx * dx + dy * dy <= 1LL * radius * radius;
    }
};
