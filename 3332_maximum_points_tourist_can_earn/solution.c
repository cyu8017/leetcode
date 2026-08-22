// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

int maxScore(int n, int k, int** stayScore, int stayScoreSize, int* stayScoreColSize, int** travelScore, int travelScoreSize, int* travelScoreColSize) {
    (void)stayScoreSize; (void)stayScoreColSize; (void)travelScoreSize; (void)travelScoreColSize;
    int* dp = (int*)calloc((size_t)n, sizeof(int));
    for (int day = 0; day < k; day++) {
        int* ndp = (int*)malloc((size_t)n * sizeof(int));
        for (int i = 0; i < n; i++) ndp[i] = INT_MIN / 4;
        for (int dest = 0; dest < n; dest++) {
            int best = INT_MIN / 4;
            for (int src = 0; src < n; src++) {
                int val = dp[src];
                if (src == dest) val += stayScore[day][dest];
                else val += travelScore[src][dest];
                if (val > best) best = val;
            }
            ndp[dest] = best;
        }
        free(dp); dp = ndp;
    }
    int ans = dp[0];
    for (int i = 1; i < n; i++) if (dp[i] > ans) ans = dp[i];
    free(dp);
    return ans;
}
