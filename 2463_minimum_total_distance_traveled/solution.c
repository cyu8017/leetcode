// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

#include <stdlib.h>
#include <string.h>

static int cmp_int(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

static int cmp_fac(const void* a, const void* b) {
    int* const* aa = (int* const*)a;
    int* const* bb = (int* const*)b;
    return (*aa)[0] - (*bb)[0];
}

long long minimumTotalDistance(int* robot, int robotSize, int** factory, int factorySize, int* factoryColSize) {
    (void)factoryColSize;
    qsort(robot, (size_t)robotSize, sizeof(int), cmp_int);
    qsort(factory, (size_t)factorySize, sizeof(int*), cmp_fac);
    int m = robotSize;
    int* pos = (int*)malloc((size_t)(factorySize * 100 + 5) * sizeof(int));
    int n = 0;
    for (int i = 0; i < factorySize; i++) {
        for (int c = 0; c < factory[i][1]; c++) pos[n++] = factory[i][0];
    }
    long long INF = 1LL << 60;
    long long** dp = (long long**)malloc((size_t)(m + 1) * sizeof(long long*));
    for (int i = 0; i <= m; i++) {
        dp[i] = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
        for (int j = 0; j <= n; j++) dp[i][j] = INF;
    }
    for (int j = 0; j <= n; j++) dp[0][j] = 0;
    for (int i = 1; i <= m; i++) {
        for (int j = i; j <= n; j++) {
            dp[i][j] = dp[i][j - 1];
            long long diff = robot[i - 1] - pos[j - 1];
            if (diff < 0) diff = -diff;
            if (dp[i - 1][j - 1] + diff < dp[i][j]) dp[i][j] = dp[i - 1][j - 1] + diff;
        }
    }
    long long ans = dp[m][n];
    for (int i = 0; i <= m; i++) free(dp[i]);
    free(dp); free(pos);
    return ans;
}
