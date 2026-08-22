// LeetCode 3809 - Best Reachable Tower
// https://leetcode.com/problems/best-reachable-tower/

#include <stdlib.h>

static int abs_i(int x) { return x < 0 ? -x : x; }

int* bestTower(int** towers, int towersSize, int* towersColSize, int* center, int centerSize, int radius, int* returnSize) {
    (void)towersColSize; (void)centerSize;
    int cx = center[0], cy = center[1];
    int idx = -1;
    for (int i = 0; i < towersSize; i++) {
        int x = towers[i][0], y = towers[i][1], q = towers[i][2];
        int dist = abs_i(x - cx) + abs_i(y - cy);
        if (dist > radius) continue;
        if (idx == -1 || towers[idx][2] < q ||
            (towers[idx][2] == q && (x < towers[idx][0] || (x == towers[idx][0] && y < towers[idx][1])))) {
            idx = i;
        }
    }
    int* ans = (int*)malloc(2 * sizeof(int));
    if (idx == -1) { ans[0] = -1; ans[1] = -1; }
    else { ans[0] = towers[idx][0]; ans[1] = towers[idx][1]; }
    *returnSize = 2;
    return ans;
}
