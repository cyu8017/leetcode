// LeetCode 1478 - Allocate Mailboxes
// https://leetcode.com/problems/allocate-mailboxes/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int minDistance(int* houses, int housesSize, int k) {
    qsort(houses, housesSize, sizeof(int), cmp_int);
    int n = housesSize;
    int** cost = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        cost[i] = (int*)calloc(n, sizeof(int));
        for (int j = i; j < n; j++) {
            int mid = houses[(i + j) / 2];
            int s = 0;
            for (int t = i; t <= j; t++) s += houses[t] > mid ? houses[t] - mid : mid - houses[t];
            cost[i][j] = s;
        }
    }
    long long INF = 1000000000000000LL;
    long long* dp = (long long*)malloc((n + 1) * sizeof(long long));
    dp[0] = 0;
    for (int i = 1; i <= n; i++) dp[i] = INF;
    for (int box = 0; box < k; box++) {
        long long* ndp = (long long*)malloc((n + 1) * sizeof(long long));
        ndp[0] = 0;
        for (int j = 1; j <= n; j++) {
            ndp[j] = INF;
            for (int i = 0; i < j; i++) {
                long long cand = dp[i] + cost[i][j - 1];
                if (cand < ndp[j]) ndp[j] = cand;
            }
        }
        free(dp); dp = ndp;
    }
    int ans = (int)dp[n];
    free(dp);
    for (int i = 0; i < n; i++) free(cost[i]);
    free(cost);
    return ans;
}
