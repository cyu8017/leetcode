// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }
static int cmp_ll(const void* a, const void* b) {
    long long x = *(const long long*)a, y = *(const long long*)b;
    return (x > y) - (x < y);
}

long long* minimumRelativeLosses(int* prices, int pricesSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    qsort(prices, pricesSize, sizeof(int), cmp_int);
    int n = pricesSize;
    long long* ans = (long long*)malloc(queriesSize * sizeof(long long));
    long long* losses = (long long*)malloc(n * sizeof(long long));
    for (int qi = 0; qi < queriesSize; qi++) {
        int k = queries[qi][0], m = queries[qi][1];
        for (int i = 0; i < n; i++) {
            if (prices[i] <= k) losses[i] = prices[i];
            else losses[i] = 2LL * k - prices[i];
        }
        qsort(losses, n, sizeof(long long), cmp_ll);
        long long sum = 0;
        for (int i = 0; i < m; i++) sum += losses[i];
        ans[qi] = sum;
    }
    free(losses);
    *returnSize = queriesSize;
    return ans;
}
