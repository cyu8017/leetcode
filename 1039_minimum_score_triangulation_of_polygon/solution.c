// LeetCode 1039 - Minimum Score Triangulation of Polygon
// https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

#include <limits.h>
#include <stdlib.h>
#include <string.h>

int minScoreTriangulation(int* values, int valuesSize) {
    int n = valuesSize;
    int* dp = (int*)calloc((size_t)n * n, sizeof(int));
    for (int len = 2; len < n; len++) {
        for (int i = 0; i + len < n; i++) {
            int j = i + len;
            int best = INT_MAX;
            for (int k = i + 1; k < j; k++) {
                int cost = dp[i * n + k] + values[i] * values[k] * values[j] + dp[k * n + j];
                if (cost < best) best = cost;
            }
            dp[i * n + j] = best;
        }
    }
    int ans = dp[0 * n + (n - 1)];
    free(dp);
    return ans;
}
