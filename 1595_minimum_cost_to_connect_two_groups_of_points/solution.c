// LeetCode 1595 - Minimum Cost to Connect Two Groups of Points
// https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

#include <stdlib.h>

int connectTwoGroups(int** cost, int costSize, int* costColSize) {
    int m = costSize, n = costColSize[0];
    int full = 1 << n;
    int INF = 1000000000;
    int* dp = (int*)malloc((size_t)full * sizeof(int));
    int* nxt = (int*)malloc((size_t)full * sizeof(int));
    for (int i = 0; i < full; i++) dp[i] = INF;
    dp[0] = 0;
    for (int r = 0; r < m; r++) {
        for (int i = 0; i < full; i++) nxt[i] = INF;
        for (int mask = 0; mask < full; mask++) {
            if (dp[mask] >= INF) continue;
            for (int j = 0; j < n; j++) {
                int new_mask = mask | (1 << j);
                int cand1 = dp[mask] + cost[r][j];
                int cand2 = nxt[mask] + cost[r][j];
                if (cand1 < nxt[new_mask]) nxt[new_mask] = cand1;
                if (cand2 < nxt[new_mask]) nxt[new_mask] = cand2;
            }
        }
        int* tmp = dp; dp = nxt; nxt = tmp;
    }
    int* minimum = (int*)malloc((size_t)n * sizeof(int));
    for (int j = 0; j < n; j++) {
        minimum[j] = cost[0][j];
        for (int i = 1; i < m; i++) if (cost[i][j] < minimum[j]) minimum[j] = cost[i][j];
    }
    int ans = INF;
    for (int mask = 0; mask < full; mask++) {
        int extra = 0;
        for (int j = 0; j < n; j++) if (!(mask & (1 << j))) extra += minimum[j];
        int cand = dp[mask] + extra;
        if (cand < ans) ans = cand;
    }
    free(dp); free(nxt); free(minimum);
    return ans;
}
