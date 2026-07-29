// LeetCode 1401 - Circle and Rectangle Overlapping
// https://leetcode.com/problems/circle-and-rectangle-overlapping/

#include <stdbool.h>

bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
    int x = xCenter < x1 ? x1 : (xCenter > x2 ? x2 : xCenter);
    int y = yCenter < y1 ? y1 : (yCenter > y2 ? y2 : yCenter);
    long long dx = x - xCenter, dy = y - yCenter;
    return dx * dx + dy * dy <= (long long)radius * radius;
}
