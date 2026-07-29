// LeetCode 1931 - Painting a Grid With Three Different Colors
// https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

#include <stdlib.h>
#include <string.h>

static int validColumn(int mask, int m) {
    int prev = -1;
    for (int i = 0; i < m; i++) {
        int c = mask % 3;
        if (c == prev) return 0;
        prev = c;
        mask /= 3;
    }
    return 1;
}

static void getColors(int mask, int m, int* out) {
    for (int i = 0; i < m; i++) {
        out[i] = mask % 3;
        mask /= 3;
    }
}

int colorTheGrid(int m, int n) {
    const int MOD = 1000000007;
    int total = 1;
    for (int i = 0; i < m; i++) total *= 3;
    int* states = (int*)malloc((size_t)total * sizeof(int));
    int sc = 0;
    for (int s = 0; s < total; s++) if (validColumn(s, m)) states[sc++] = s;
    int** compat = (int**)malloc((size_t)sc * sizeof(int*));
    int* compatSz = (int*)calloc((size_t)sc, sizeof(int));
    int ca[5], cb[5];
    for (int i = 0; i < sc; i++) {
        compat[i] = (int*)malloc((size_t)sc * sizeof(int));
        getColors(states[i], m, ca);
        for (int j = 0; j < sc; j++) {
            getColors(states[j], m, cb);
            int ok = 1;
            for (int k = 0; k < m; k++) if (ca[k] == cb[k]) { ok = 0; break; }
            if (ok) compat[i][compatSz[i]++] = j;
        }
    }
    long long* dp = (long long*)calloc((size_t)sc, sizeof(long long));
    long long* ndp = (long long*)calloc((size_t)sc, sizeof(long long));
    for (int i = 0; i < sc; i++) dp[i] = 1;
    for (int col = 1; col < n; col++) {
        memset(ndp, 0, (size_t)sc * sizeof(long long));
        for (int i = 0; i < sc; i++) {
            if (!dp[i]) continue;
            for (int t = 0; t < compatSz[i]; t++) {
                int j = compat[i][t];
                ndp[j] = (ndp[j] + dp[i]) % MOD;
            }
        }
        long long* tmp = dp; dp = ndp; ndp = tmp;
    }
    long long ans = 0;
    for (int i = 0; i < sc; i++) ans = (ans + dp[i]) % MOD;
    for (int i = 0; i < sc; i++) free(compat[i]);
    free(compat); free(compatSz); free(states); free(dp); free(ndp);
    return (int)ans;
}
