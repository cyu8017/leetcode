// LeetCode 1620 - Coordinate With Maximum Network Quality
// https://leetcode.com/problems/coordinate-with-maximum-network-quality/

#include <stdlib.h>
#include <math.h>

int* bestCoordinate(int** towers, int towersSize, int* towersColSize, int radius, int* returnSize) {
    (void)towersColSize;
    int bestX = 0, bestY = 0, bestQ = -1;
    for (int x = 0; x <= 50; x++) {
        for (int y = 0; y <= 50; y++) {
            int q = 0;
            for (int i = 0; i < towersSize; i++) {
                double d = hypot(x - towers[i][0], y - towers[i][1]);
                if (d <= radius) q += (int)(towers[i][2] / (1.0 + d));
            }
            if (q > bestQ) {
                bestQ = q;
                bestX = x;
                bestY = y;
            }
        }
    }
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = bestX; ans[1] = bestY;
    *returnSize = 2;
    return ans;
}
