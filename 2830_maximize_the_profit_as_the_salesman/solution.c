// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

#include <stdlib.h>

int maximizeTheProfit(int n, int** offers, int offersSize, int* offersColSize) {
    (void)offersColSize;
    int* dp = (int*)calloc(n + 1, sizeof(int));
    // group by end: store indices
    int* cnt = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < offersSize; i++) cnt[offers[i][1]]++;
    int** byEnd = (int**)malloc(n * sizeof(int*));
    int* fill = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++) byEnd[i] = (int*)malloc(cnt[i] * sizeof(int));
    for (int i = 0; i < offersSize; i++) {
        int e = offers[i][1];
        byEnd[e][fill[e]++] = i;
    }
    for (int end = 0; end < n; end++) {
        dp[end + 1] = dp[end];
        for (int t = 0; t < fill[end]; t++) {
            int* o = offers[byEnd[end][t]];
            int cand = dp[o[0]] + o[2];
            if (cand > dp[end + 1]) dp[end + 1] = cand;
        }
    }
    int ans = dp[n];
    for (int i = 0; i < n; i++) free(byEnd[i]);
    free(byEnd); free(cnt); free(fill); free(dp);
    return ans;
}
