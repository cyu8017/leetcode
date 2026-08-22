// LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

#include <stdlib.h>

int maxProfit(int n, int** edges, int edgesSize, int* edgesColSize, int* score, int scoreSize) {
    (void)edgesColSize; (void)scoreSize;
    int* need = (int*)calloc((size_t)n, sizeof(int));
    int N = 1 << n;
    int* dp = (int*)malloc((size_t)N * sizeof(int));
    for (int i = 0; i < N; i++) dp[i] = -1;
    dp[0] = 0;
    for (int i = 0; i < edgesSize; i++) need[edges[i][1]] |= 1 << edges[i][0];
    for (int mask = 0; mask < N; mask++) {
        if (dp[mask] < 0) continue;
        int pos = 0, x = mask;
        while (x) { pos += x & 1; x >>= 1; }
        pos++;
        for (int i = 0; i < n; i++) {
            if ((mask >> i) & 1) continue;
            if ((mask & need[i]) == need[i]) {
                int nm = mask | (1 << i);
                int v = dp[mask] + score[i] * pos;
                if (v > dp[nm]) dp[nm] = v;
            }
        }
    }
    int ans = dp[N - 1];
    free(need); free(dp);
    return ans;
}
