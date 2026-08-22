// LeetCode 2280 - Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

#include <stdlib.h>

static int cmp_pair(const void* a, const void* b) {
    int* const* pa = (int* const*)a;
    int* const* pb = (int* const*)b;
    return (*pa)[0] - (*pb)[0];
}

int minimumLines(int** stockPrices, int stockPricesSize, int* stockPricesColSize) {
    (void)stockPricesColSize;
    if (stockPricesSize <= 1) return 0;
    qsort(stockPrices, (size_t)stockPricesSize, sizeof(int*), cmp_pair);
    int ans = 1;
    for (int i = 2; i < stockPricesSize; i++) {
        long long x0 = stockPrices[i - 2][0], y0 = stockPrices[i - 2][1];
        long long x1 = stockPrices[i - 1][0], y1 = stockPrices[i - 1][1];
        long long x2 = stockPrices[i][0], y2 = stockPrices[i][1];
        if ((y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0)) {
            ans++;
        }
    }
    return ans;
}
