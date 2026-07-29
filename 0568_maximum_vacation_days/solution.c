// LeetCode 0568 - Maximum Vacation Days
// https://leetcode.com/problems/maximum-vacation-days/

#include <stdlib.h>

int maxVacationDays(int** flights, int flightsSize, int* flightsColSize, int** days, int daysSize, int* daysColSize) {
    (void)flightsColSize;
    (void)daysSize;
    int cities = flightsSize;
    int weeks = daysColSize[0];
    const int NEG = -1000000000;

    int* dp = (int*)malloc((size_t)cities * sizeof(int));
    int* nxt = (int*)malloc((size_t)cities * sizeof(int));
    for (int i = 0; i < cities; i++) {
        dp[i] = NEG;
    }
    dp[0] = 0;

    for (int week = 0; week < weeks; week++) {
        for (int i = 0; i < cities; i++) {
            nxt[i] = NEG;
        }
        for (int city = 0; city < cities; city++) {
            if (dp[city] == NEG) {
                continue;
            }
            for (int dest = 0; dest < cities; dest++) {
                if (dest == city || flights[city][dest]) {
                    int candidate = dp[city] + days[dest][week];
                    if (candidate > nxt[dest]) {
                        nxt[dest] = candidate;
                    }
                }
            }
        }
        int* tmp = dp;
        dp = nxt;
        nxt = tmp;
    }

    int best = NEG;
    for (int i = 0; i < cities; i++) {
        if (dp[i] > best) {
            best = dp[i];
        }
    }
    free(dp);
    free(nxt);
    return best;
}
