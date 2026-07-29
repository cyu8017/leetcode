// LeetCode 0813 - Largest Sum of Averages
// https://leetcode.com/problems/largest-sum-of-averages/

#include <stdlib.h>

#define MAX(a,b) ((a)>(b)?(a):(b))

double largestSumOfAverages(int* nums, int numsSize, int k) {
    int n = numsSize;
    double* prefix = (double*)calloc((size_t)n + 1, sizeof(double));
    for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
    double* dp = (double*)malloc((size_t)n * sizeof(double));
    for (int i = 0; i < n; i++) dp[i] = (prefix[i + 1] - prefix[0]) / (i + 1);
    for (int groups = 2; groups <= k; groups++) {
        double* nxt = (double*)calloc((size_t)n, sizeof(double));
        for (int i = groups - 1; i < n; i++) {
            double best = 0.0;
            for (int j = groups - 2; j < i; j++) {
                double avg = (prefix[i + 1] - prefix[j + 1]) / (i - j);
                best = MAX(best, dp[j] + avg);
            }
            nxt[i] = best;
        }
        free(dp);
        dp = nxt;
    }
    double ans = dp[n - 1];
    free(dp); free(prefix);
    return ans;
}
