// LeetCode 0469 - Convex Polygon
// https://leetcode.com/problems/convex-polygon/

#include <stdbool.h>

bool isConvex(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    int direction = 0;
    for (int index = 0; index < pointsSize; index++) {
        long long x1 = (long long)points[(index + 1) % pointsSize][0] - points[index][0];
        long long y1 = (long long)points[(index + 1) % pointsSize][1] - points[index][1];
        long long x2 = (long long)points[(index + 2) % pointsSize][0] - points[(index + 1) % pointsSize][0];
        long long y2 = (long long)points[(index + 2) % pointsSize][1] - points[(index + 1) % pointsSize][1];
        long long cross = x1 * y2 - y1 * x2;
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
