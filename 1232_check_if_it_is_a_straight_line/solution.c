// LeetCode 1232 - Check If It Is a Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

#include <stdbool.h>

bool checkStraightLine(int** coordinates, int coordinatesSize, int* coordinatesColSize) {
    (void)coordinatesSize;
    (void)coordinatesColSize;
    long long x0 = coordinates[0][0];
    long long y0 = coordinates[0][1];
    long long dx = coordinates[1][0] - x0;
    long long dy = coordinates[1][1] - y0;
    for (int i = 2; i < coordinatesSize; i++) {
        long long x = coordinates[i][0];
        long long y = coordinates[i][1];
        if ((x - x0) * dy != (y - y0) * dx) return false;
    }
    return true;
}
