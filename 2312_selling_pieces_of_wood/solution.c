// LeetCode 2312 - Selling Pieces of Wood
// https://leetcode.com/problems/selling-pieces-of-wood/

#include <stdlib.h>
#include <string.h>

long long sellingWood(int m, int n, int** prices, int pricesSize, int* pricesColSize) {
    (void)pricesColSize;
    long long** price = (long long**)malloc((size_t)(m + 1) * sizeof(long long*));
    long long** dp = (long long**)malloc((size_t)(m + 1) * sizeof(long long*));
    for (int i = 0; i <= m; i++) {
        price[i] = (long long*)calloc((size_t)(n + 1), sizeof(long long));
        dp[i] = (long long*)calloc((size_t)(n + 1), sizeof(long long));
    }
    for (int i = 0; i < pricesSize; i++) {
        price[prices[i][0]][prices[i][1]] = prices[i][2];
    }
    for (int h = 1; h <= m; h++) {
        for (int w = 1; w <= n; w++) {
            long long best = price[h][w];
            for (int i = 1; i < h; i++) {
                if (dp[i][w] + dp[h - i][w] > best) best = dp[i][w] + dp[h - i][w];
            }
            for (int j = 1; j < w; j++) {
                if (dp[h][j] + dp[h][w - j] > best) best = dp[h][j] + dp[h][w - j];
            }
            dp[h][w] = best;
        }
    }
    long long ans = dp[m][n];
    for (int i = 0; i <= m; i++) { free(price[i]); free(dp[i]); }
    free(price); free(dp);
    return ans;
}
