// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

#include <stdlib.h>

#define INF3538 (1000000000000000000LL)

static int n3538, k3538;
static int *pos3538, *pref3538;
static long long ***memo3538;
static char ***seen3538;

static long long dp3538(int i, int skips, int last) {
    if (i == n3538 - 1) return skips == 0 ? 0 : INF3538;
    if (seen3538[i][skips][last]) return memo3538[i][skips][last];
    seen3538[i][skips][last] = 1;
    long long rate = pref3538[i];
    if (last > 0) rate -= pref3538[last - 1];
    long long res = INF3538;
    int end = n3538 - 1;
    if (i + skips + 1 < end) end = i + skips + 1;
    for (int j = i + 1; j <= end; j++) {
        long long cand = (long long)(pos3538[j] - pos3538[i]) * rate + dp3538(j, skips - (j - i - 1), i + 1);
        if (cand < res) res = cand;
    }
    memo3538[i][skips][last] = res;
    return res;
}

long long minTravelTime(int l, int n, int k, int* position, int positionSize, int* time, int timeSize) {
    (void)l; (void)positionSize; (void)timeSize;
    n3538 = n; k3538 = k; pos3538 = position;
    pref3538 = (int*)malloc((size_t)n * sizeof(int));
    pref3538[0] = time[0];
    for (int i = 1; i < n; i++) pref3538[i] = pref3538[i - 1] + time[i];
    memo3538 = (long long***)malloc((size_t)n * sizeof(long long**));
    seen3538 = (char***)malloc((size_t)n * sizeof(char**));
    for (int i = 0; i < n; i++) {
        memo3538[i] = (long long**)malloc((size_t)(k + 1) * sizeof(long long*));
        seen3538[i] = (char**)malloc((size_t)(k + 1) * sizeof(char*));
        for (int j = 0; j <= k; j++) {
            memo3538[i][j] = (long long*)calloc((size_t)n, sizeof(long long));
            seen3538[i][j] = (char*)calloc((size_t)n, 1);
        }
    }
    long long ans = dp3538(0, k, 0);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= k; j++) { free(memo3538[i][j]); free(seen3538[i][j]); }
        free(memo3538[i]); free(seen3538[i]);
    }
    free(memo3538); free(seen3538); free(pref3538);
    return ans;
}
