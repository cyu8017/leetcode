// LeetCode 0256 - Paint House
// https://leetcode.com/problems/paint-house/

#include <stdlib.h>

static int min_int(int a, int b) {
    return a < b ? a : b;
}

int minCost(int** costs, int costsSize, int* costsColSize) {
    (void)costsColSize;
    if (costsSize == 0) {
        return 0;
    }
    int previous[3] = { costs[0][0], costs[0][1], costs[0][2] };
    for (int row = 1; row < costsSize; row++) {
        int color0 = costs[row][0] + min_int(previous[1], previous[2]);
        int color1 = costs[row][1] + min_int(previous[0], previous[2]);
        int color2 = costs[row][2] + min_int(previous[0], previous[1]);
        previous[0] = color0;
        previous[1] = color1;
        previous[2] = color2;
    }
    return min_int(previous[0], min_int(previous[1], previous[2]));
}
