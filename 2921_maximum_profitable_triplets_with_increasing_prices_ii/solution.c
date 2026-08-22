// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

#include <stdlib.h>
#include <string.h>

int maxProfit(int* prices, int pricesSize, int* profits, int profitsSize) {
    (void)profitsSize;
    int n = pricesSize, ans = -1;
    int* bit = (int*)calloc(5002, sizeof(int));
    int* maxLeft = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < 5002; i++) bit[i] = -1;
    for (int j = 0; j < n; j++) {
        int best = -1, i = prices[j] - 1;
        while (i > 0) { if (bit[i] > best) best = bit[i]; i -= i & -i; }
        maxLeft[j] = best;
        int val = profits[j], idx = prices[j];
        while (idx < 5002) { if (val > bit[idx]) bit[idx] = val; idx += idx & -idx; }
    }
    for (int j = 0; j < n; j++) {
        int bestR = -1;
        for (int k = j + 1; k < n; k++)
            if (prices[k] > prices[j] && profits[k] > bestR) bestR = profits[k];
        if (maxLeft[j] >= 0 && bestR >= 0) {
            int cand = maxLeft[j] + profits[j] + bestR;
            if (cand > ans) ans = cand;
        }
    }
    free(bit); free(maxLeft);
    return ans;
}
