// LeetCode 0188 - Best Time to Buy and Sell Stock IV
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

#include <limits.h>
#include <stdlib.h>

int maxProfit(int k, int* prices, int pricesSize) {
    if (pricesSize == 0 || k == 0) {
        return 0;
    }
    if (k >= pricesSize / 2) {
        int profit = 0;
        for (int i = 1; i < pricesSize; ++i) {
            if (prices[i] > prices[i - 1]) {
                profit += prices[i] - prices[i - 1];
            }
        }
        return profit;
    }

    int* buy = malloc((k + 1) * sizeof(*buy));
    int* sell = calloc(k + 1, sizeof(*sell));
    for (int transaction = 1; transaction <= k; ++transaction) {
        buy[transaction] = INT_MAX;
    }
    for (int i = 0; i < pricesSize; ++i) {
        for (int transaction = 1; transaction <= k; ++transaction) {
            int candidateBuy = prices[i] - sell[transaction - 1];
            if (candidateBuy < buy[transaction]) {
                buy[transaction] = candidateBuy;
            }
            int candidateSell = prices[i] - buy[transaction];
            if (candidateSell > sell[transaction]) {
                sell[transaction] = candidateSell;
            }
        }
    }

    int result = sell[k];
    free(buy);
    free(sell);
    return result;
}