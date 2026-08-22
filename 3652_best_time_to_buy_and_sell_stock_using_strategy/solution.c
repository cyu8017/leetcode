// LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

#include <stdlib.h>
static long long llmax(long long a,long long b){return a>b?a:b;}
long long maxProfit(int* prices, int pricesSize, int* strategy, int strategySize, int k) {
    (void)strategySize;
    int n = pricesSize;
    long long* s = (long long*)calloc((size_t)n + 1, sizeof(long long));
    long long* t = (long long*)calloc((size_t)n + 1, sizeof(long long));
    for (int i = 1; i <= n; i++) {
        s[i] = s[i - 1] + (long long)prices[i - 1] * strategy[i - 1];
        t[i] = t[i - 1] + prices[i - 1];
    }
    long long ans = s[n];
    for (int i = k; i <= n; i++)
        ans = llmax(ans, s[n] - (s[i] - s[i - k]) + (t[i] - t[i - k / 2]));
    free(s); free(t);
    return ans;
}
