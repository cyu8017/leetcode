// LeetCode 3573 - Best Time to Buy and Sell Stock V
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

#include <stdlib.h>
#include <string.h>

static long long llmax(long long a, long long b) { return a > b ? a : b; }
static long long llmax3(long long a, long long b, long long c) { return llmax(a, llmax(b, c)); }

long long maximumProfit(int* prices, int pricesSize, int k) {
    int n = pricesSize;
    long long*** f = (long long***)malloc((size_t)n * sizeof(long long**));
    for (int i = 0; i < n; i++) {
        f[i] = (long long**)malloc((size_t)(k + 1) * sizeof(long long*));
        for (int j = 0; j <= k; j++) {
            f[i][j] = (long long*)calloc(3, sizeof(long long));
        }
    }
    for (int j = 1; j <= k; j++) {
        f[0][j][1] = -prices[0];
        f[0][j][2] = prices[0];
    }
    for (int i = 1; i < n; i++) {
        for (int j = 1; j <= k; j++) {
            f[i][j][0] = llmax3(f[i - 1][j][0], f[i - 1][j][1] + prices[i], f[i - 1][j][2] - prices[i]);
            f[i][j][1] = llmax(f[i - 1][j][1], f[i - 1][j - 1][0] - prices[i]);
            f[i][j][2] = llmax(f[i - 1][j][2], f[i - 1][j - 1][0] + prices[i]);
        }
    }
    long long ans = f[n - 1][k][0];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= k; j++) free(f[i][j]);
        free(f[i]);
    }
    free(f);
    return ans;
}
