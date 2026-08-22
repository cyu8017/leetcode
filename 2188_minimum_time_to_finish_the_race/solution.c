// LeetCode 2188 - Minimum Time to Finish the Race
// https://leetcode.com/problems/minimum-time-to-finish-the-race/

#include <stdlib.h>

int minimumFinishTime(int** tires, int tiresSize, int* tiresColSize, int changeTime, int numLaps) {
    (void)tiresColSize;
    int minTime[20];
    for (int i = 0; i < 20; i++) minTime[i] = 1 << 30;
    for (int i = 0; i < tiresSize; i++) {
        int f = tires[i][0], r = tires[i][1];
        int t = f, lap = f;
        for (int x = 1; x < 20 && t < minTime[x]; x++) {
            minTime[x] = t;
            lap *= r;
            if (lap > changeTime + f) break;
            t += lap;
        }
    }
    int* dp = (int*)malloc((size_t)(numLaps + 1) * sizeof(int));
    for (int i = 0; i <= numLaps; i++) dp[i] = 1 << 30;
    dp[0] = -changeTime;
    for (int i = 1; i <= numLaps; i++) {
        for (int j = 1; j <= i && j < 20; j++) {
            int cand = dp[i - j] + changeTime + minTime[j];
            if (cand < dp[i]) dp[i] = cand;
        }
    }
    int ans = dp[numLaps];
    free(dp);
    return ans;
}
