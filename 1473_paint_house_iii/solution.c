// LeetCode 1473 - Paint House III
// https://leetcode.com/problems/paint-house-iii/

#include <stdlib.h>
#include <limits.h>

int minCost(int* houses, int housesSize, int** cost, int costSize, int* costColSize, int m, int n, int target) {
    (void)costSize; (void)costColSize; (void)m;
    long long INF = LLONG_MAX / 4;
    // map (prev, groups) -> value using arrays of size (n+1)*(target+1)
    long long* dp = (long long*)malloc((n + 1) * (target + 1) * sizeof(long long));
    for (int i = 0; i < (n + 1) * (target + 1); i++) dp[i] = INF;
    dp[0 * (target + 1) + 0] = 0;
    for (int i = 0; i < housesSize; i++) {
        long long* nxt = (long long*)malloc((n + 1) * (target + 1) * sizeof(long long));
        for (int t = 0; t < (n + 1) * (target + 1); t++) nxt[t] = INF;
        int painted = houses[i];
        for (int prev = 0; prev <= n; prev++) {
            for (int groups = 0; groups <= target; groups++) {
                if (dp[prev * (target + 1) + groups] >= INF) continue;
                if (painted) {
                    int color = painted;
                    int ng = groups + (color != prev);
                    if (ng <= target) {
                        long long nv = dp[prev * (target + 1) + groups];
                        if (nv < nxt[color * (target + 1) + ng]) nxt[color * (target + 1) + ng] = nv;
                    }
                } else {
                    for (int color = 1; color <= n; color++) {
                        int ng = groups + (color != prev);
                        if (ng <= target) {
                            long long nv = dp[prev * (target + 1) + groups] + cost[i][color - 1];
                            if (nv < nxt[color * (target + 1) + ng]) nxt[color * (target + 1) + ng] = nv;
                        }
                    }
                }
            }
        }
        free(dp); dp = nxt;
    }
    long long ans = INF;
    for (int c = 1; c <= n; c++) if (dp[c * (target + 1) + target] < ans) ans = dp[c * (target + 1) + target];
    free(dp);
    return ans >= INF ? -1 : (int)ans;
}
