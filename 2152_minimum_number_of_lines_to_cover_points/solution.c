// LeetCode 2152 - Minimum Number of Lines to Cover Points
// https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/

#include <stdlib.h>

static int colinear(int* a, int* b, int* c) {
    return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1]);
}

int minimumLines(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    int n = pointsSize;
    if (n <= 2) return 1;
    int inf = n, N = 1 << n;
    int* dp = (int*)malloc((size_t)N * sizeof(int));
    for (int i = 0; i < N; i++) dp[i] = inf;
    dp[0] = 0;
    for (int mask = 0; mask < N; mask++) {
        if (dp[mask] == inf) continue;
        int i = 0;
        while (i < n && (mask & (1 << i))) i++;
        if (i == n) continue;
        int nm = mask | (1 << i);
        if (dp[mask] + 1 < dp[nm]) dp[nm] = dp[mask] + 1;
        for (int j = i + 1; j < n; j++) {
            if (mask & (1 << j)) continue;
            nm = mask | (1 << i) | (1 << j);
            for (int k = 0; k < n; k++) {
                if ((nm & (1 << k)) == 0 && colinear(points[i], points[j], points[k]))
                    nm |= 1 << k;
            }
            if (dp[mask] + 1 < dp[nm]) dp[nm] = dp[mask] + 1;
        }
    }
    int ans = dp[N - 1];
    free(dp);
    return ans;
}
