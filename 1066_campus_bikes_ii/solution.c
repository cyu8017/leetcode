// LeetCode 1066 - Campus Bikes II
// https://leetcode.com/problems/campus-bikes-ii/

#include <stdlib.h>
#include <string.h>

static int minDist(int i, int mask, int** workers, int workersSize, int** bikes, int bikesSize, int* memo) {
    if (i == workersSize) {
        return 0;
    }
    if (memo[mask] >= 0) {
        return memo[mask];
    }
    int best = 1000000000;
    int wx = workers[i][0], wy = workers[i][1];
    for (int b = 0; b < bikesSize; b++) {
        if (mask & (1 << b)) {
            continue;
        }
        int dist = abs(wx - bikes[b][0]) + abs(wy - bikes[b][1]);
        int cand = dist + minDist(i + 1, mask | (1 << b), workers, workersSize, bikes, bikesSize, memo);
        if (cand < best) {
            best = cand;
        }
    }
    memo[mask] = best;
    return best;
}

int assignBikes(int** workers, int workersSize, int* workersColSize, int** bikes, int bikesSize,
                int* bikesColSize) {
    (void)workersColSize;
    (void)bikesColSize;
    int states = 1 << bikesSize;
    int* memo = (int*)malloc((size_t)states * sizeof(int));
    for (int i = 0; i < states; i++) {
        memo[i] = -1;
    }
    int ans = minDist(0, 0, workers, workersSize, bikes, bikesSize, memo);
    free(memo);
    return ans;
}
