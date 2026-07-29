// LeetCode 1494 - Parallel Courses II
// https://leetcode.com/problems/parallel-courses-ii/

#include <stdlib.h>

static int bitcount(int x) { int c = 0; while (x) { c += x & 1; x >>= 1; } return c; }

int minNumberOfSemesters(int n, int** relations, int relationsSize, int* relationsColSize, int k) {
    (void)relationsColSize;
    int* prereq = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < relationsSize; i++)
        prereq[relations[i][1] - 1] |= 1 << (relations[i][0] - 1);
    int full = (1 << n) - 1, INF = 1000000000;
    int* dp = (int*)malloc((1 << n) * sizeof(int));
    for (int i = 0; i < (1 << n); i++) dp[i] = INF;
    dp[0] = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        if (dp[mask] == INF) continue;
        int available = 0;
        for (int c = 0; c < n; c++)
            if (!(mask & (1 << c)) && (prereq[c] & mask) == prereq[c])
                available |= 1 << c;
        if (bitcount(available) <= k) {
            int take = available;
            if (dp[mask] + 1 < dp[mask | take]) dp[mask | take] = dp[mask] + 1;
        } else {
            for (int sub = available; sub; sub = (sub - 1) & available) {
                if (bitcount(sub) == k && dp[mask] + 1 < dp[mask | sub])
                    dp[mask | sub] = dp[mask] + 1;
            }
        }
    }
    int ans = dp[full];
    free(dp); free(prereq);
    return ans;
}
