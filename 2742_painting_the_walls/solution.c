// LeetCode 2742 - Painting the Walls
// https://leetcode.com/problems/painting-the-walls/

#include <stdlib.h>

int paintWalls(int* cost, int costSize, int* time, int timeSize) {
    (void)timeSize;
    int n = costSize;
    const long long INF = 1000000000000000000LL;
    long long* dp = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    dp[0] = 0;
    for (int i = 1; i <= n; i++) dp[i] = INF;
    for (int i = 0; i < n; i++) {
        for (int j = n; j >= 0; j--) {
            int nj = j + time[i] + 1;
            if (nj > n) nj = n;
            if (dp[j] + cost[i] < dp[nj]) dp[nj] = dp[j] + cost[i];
        }
    }
    int ans = (int)dp[n];
    free(dp);
    return ans;
}
